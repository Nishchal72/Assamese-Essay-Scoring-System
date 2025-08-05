from flask import Flask, render_template, request
from preprocessing import preprocess_text
from grammar import compute_grammar_score
from spelling import compute_spelling_score_indic
from semantics import compute_semantic_score_indicbert
from lexical import compute_lexical_score, common_words_set
from scoring import aggregate_scores
from model_loader import flair_tagger

app = Flask(__name__)


from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("ai4bharat/indic-bert")
model = AutoModel.from_pretrained("ai4bharat/indic-bert")

reference_essays = [
    "অসম এখন পূৰ্ণাংগ ৰাজ্য। ইয়াত বহু জাতি-উপজাতিৰ মানুহে একেলগে বাস কৰে।",
    "অসম প্ৰাকৃতিক সম্পদত সমৃদ্ধ ৰাজ্য। ইয়াৰ ধান, চাহ আৰু তেলবিশিষ্ট খনিজ সমৃদ্ধ।",
    "অসমীয়া সংস্কৃতি আৰু পৰম্পৰা অত্যন্ত সমৃদ্ধ।"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/score', methods=['POST'])
def score():
    essay = request.form['essay']

    # Step 1: Preprocess
    cleaned_essay = preprocess_text(essay)

    # Step 2: Compute individual component scores
    #grammar_score = compute_grammar_score(cleaned_essay, flair_tagger)
    #spelling_score = compute_spelling_score_indic(cleaned_essay)
    #semantic_score = compute_semantic_score_indicbert(cleaned_essay, reference_essays, tokenizer, model)
    #lexical_score = compute_lexical_score(cleaned_essay, flair_tagger, common_words_set)

    # Step 3: Aggregate total score
    #total_score = aggregate_scores(grammar_score, spelling_score, semantic_score, lexical_score)


    # Step 2 & 3: Use aggregate_scores to compute all at once
    scores = aggregate_scores(cleaned_essay, reference_essays, flair_tagger, tokenizer, model, common_words_set)

    # Extract individual scores
    grammar_score = scores["Grammar"]
    spelling_score = scores["Spelling"]
    semantic_score = scores["Semantic"]
    lexical_score = scores["Lexical"]
    total_score = scores["Final Score"]

    return render_template(
        'result.html',
        essay=essay,
        grammar_score=grammar_score,
        spelling_score=spelling_score,
        semantic_score=semantic_score,
        lexical_score=lexical_score,
        total_score=total_score
    )

if __name__ == '__main__':
    app.run(debug=True)
