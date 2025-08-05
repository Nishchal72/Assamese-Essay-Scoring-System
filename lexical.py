import re
from flair.data import Sentence
import pandas as pd
import os
# Load Assamese common words from a CSV file
# Load the CSV from the same folder
csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "asm_wikipedia.csv"))
common_words_df = pd.read_csv(csv_path)# Make sure this file exists
common_words_set = set(common_words_df["word"].dropna().str.strip())

def tokenize_assamese(text):
    return re.findall(r'\w+', text)

def compute_rare_word_score(essay, common_words_set):
    tokens = tokenize_assamese(essay)
    if not tokens:
        return 0.0
    rare_words = [w for w in tokens if w not in common_words_set]
    rare_score = len(rare_words) / len(tokens)
    return round(min(rare_score * 10, 10.0), 2)

def compute_lexical_density(essay, tagger):
    sentence = Sentence(essay)
    tagger.predict(sentence)
    content_pos_prefixes = {"N", "V", "ADJ", "ADV", "RB"}
    total = len(sentence)
    content = 0
    for token in sentence:
        try:
            tag = token.labels[0].value
            tag_prefix = tag.split("_")[0]
            if tag_prefix in content_pos_prefixes:
                content += 1
        except:
            continue
    return round((content / total) * 10, 2) if total else 0.0

def compute_lexical_score(essay, tagger, common_words_set):
    density = compute_lexical_density(essay, tagger)
    rare = compute_rare_word_score(essay, common_words_set)
    return round(0.6 * density + 0.4 * rare, 2)
