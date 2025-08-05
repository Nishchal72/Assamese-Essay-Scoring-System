from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
from preprocessing import preprocess_text

def get_indicbert_embedding(text, tokenizer, model):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=512
    )
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings[0].numpy()

def compute_semantic_score_indicbert(essay, reference_essays, tokenizer, model):
    student_vec = get_indicbert_embedding(essay, tokenizer, model)
    ref_vecs = [get_indicbert_embedding(ref, tokenizer, model) for ref in reference_essays]
    sims = [cosine_similarity([student_vec], [ref_vec])[0][0] for ref_vec in ref_vecs]
    max_sim = max(sims)
    return round(max_sim * 10, 2)
