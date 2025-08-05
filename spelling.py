import pandas as pd
from preprocessing import normalize_text
import os


# Load the CSV from the same folder
csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "asm_wikipedia.csv"))

df = pd.read_csv(csv_path, encoding="utf-8")
vocab = set(df["word"].dropna().str.strip())
normalized_dict = set(normalize_text(word.strip()) for word in df["word"].dropna().astype(str))
#normalized_dict = set(normalize_text(word.strip()) for word in df[0].dropna().astype(str))

def compute_spelling_score_indic(essay):
    normalized_essay = normalize_text(essay)
    words = normalized_essay.split()
    total = len(words)
    incorrect = 0

    for word in words:
        if word not in normalized_dict:
            incorrect += 1

    score = round(10 * (1 - incorrect / total), 2) if total > 0 else 0
    return score
