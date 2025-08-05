from grammar import compute_grammar_score
from spelling import compute_spelling_score_indic
from semantics import compute_semantic_score_indicbert
from lexical import compute_lexical_score

def aggregate_scores(essay, references, tagger, tokenizer, model, common_words_set):
    grammar = compute_grammar_score(essay, tagger)
    spelling = compute_spelling_score_indic(essay)
    semantic = compute_semantic_score_indicbert(essay, references, tokenizer, model)
    lexical = compute_lexical_score(essay, tagger, common_words_set)

    final_score = 0.3 * grammar + 0.2 * spelling + 0.3 * semantic + 0.2 * lexical
    return {
        "Grammar": grammar,
        "Spelling": spelling,
        "Semantic": semantic,
        "Lexical": lexical,
        "Final Score": round(final_score, 2)
    }
