from flair.data import Sentence
from collections import Counter

VERB_TAGS = {"V_VM", "V_VAUX", "V_VBT", "V_VBI"}
PUNCT_TAGS = {"RD_PUNC", "RD_SYM"}
ADJ_TAGS = {"J_JJ", "J_PJJ", "J_VJJ"}

def extract_pos_features(essay, tagger):
    sentence = Sentence(essay)
    tagger.predict(sentence)

    tags = []
    for token in sentence:
        labels = token.get_labels()
        if labels:
            full_tag = labels[0].value  # like V_VM or RD_PUNC
            tags.append(full_tag)

    total = len(tags)
    count = Counter(tags)
    return {tag: count[tag] / total for tag in count}

def compute_grammar_score(essay, tagger):
    features = extract_pos_features(essay, tagger)
    score = 0

    verb_score = sum(features.get(tag, 0) for tag in VERB_TAGS)
    punct_penalty = sum(features.get(tag, 0) for tag in PUNCT_TAGS)
    adj_score = sum(features.get(tag, 0) for tag in ADJ_TAGS)

    score += verb_score * 15
    score += adj_score * 5
    score -= punct_penalty * 1

    score += len(features.keys()) * 0.5  # reward diversity

    return round(max(0, min(10, score)), 2)
