# Assamese-Essay-Scoring-System
The Assamese Essay Scoring App is an intelligent automated evaluation system designed specifically for essays written in the Assamese language. Leveraging the power of Natural Language Processing (NLP), the system combines multiple advanced components to assess essays based on grammar, semantics, spelling, and lexical quality.
## 🚀 Features

- ✅ Grammar analysis using Assamese POS tagging (AsPOS)
- ✅ Spelling checker using dictionary matching
- ✅ Semantic understanding using IndicBERT embeddings
- ✅ Lexical score is given on the basis of uniqueness of the words
- ✅ Easy-to-use Flask web interface.

- ## 🧠 Technologies Used

| Tool/Library         | Purpose                                                             |
|----------------------|---------------------------------------------------------------------|
| **Flask**            | Backend web application framework                                  |
| **AsPOS.pt**         | Pre-trained Assamese POS tagger for grammar analysis               |
| **Indic NLP Library**| Sentence & word tokenization, text normalization for Assamese       |
| **IndicBERT**        | Transformer-based model for semantic embedding of Assamese text     |                       
| **Torch & Transformers** | Backend for loading and running deep learning models           |

## 🧠 Models Used

This project uses a combination of transformer models, POS taggers, and classical machine learning to evaluate Assamese essays comprehensively.

---

### 1. 🚀 IndicBERT (Semantic Scoring)

- **Model:** [`ai4bharat/indic-bert`](https://huggingface.co/ai4bharat/indic-bert)
- **Type:** Multilingual ALBERT-based Transformer
- **Use Case:** Generates contextual embeddings for Assamese sentences.
- **Application:** Measures semantic similarity between essays and reference material.

---

### 2. 🧠 AsPOS Tagger (Grammar Scoring)

- **Model:** [`dpathak/aspos_assamese_pos_tagger`](https://huggingface.co/dpathak/aspos_assamese_pos_tagger)
- **Architecture:** BiLSTM-CRF with MuRIL + Flair Embeddings
- **Use Case:** Assigns POS tags to Assamese tokens.
- **Application:** Evaluates grammatical structure, correctness, and POS tag diversity.

---

### 3. 📚 Indic NLP Library (Lexical Analysis & Preprocessing)

- **Repository:** [Indic NLP Library](https://github.com/anoopkunchukuttan/indic_nlp_library)
- **Tools Used:**
  - Sentence segmentation
  - Word tokenization
  - Script normalization
- **Application:** Preprocesses Assamese text for grammar scoring, spelling checks, and readability metrics.

---

## Installation & Setup

- 1. Clone the Repository
     - git clone https://github.com/nishchaldas9859/Assamese-Essay-Scoring-System.git
        cd Assamese-Essay-Scoring-System
- 2. Install Python Dependencies
     - pip install -r requirements.txt
- 3. Download AsPOS Model (Assamese POS Tagger)
     - Go to: https://huggingface.co/dpathak/aspos_assamese_pos_tagger
- 4. Download Indic NLP Resources
     - git clone https://github.com/anoopkunchukuttan/indic_nlp_resources.git
- 5. Run the Flask App
     - python run.py

## 🙏 Credits & Acknowledgments

This project builds upon the work of several open-source contributors and research teams. We sincerely thank the following for their valuable tools and models:

---

### 🔤 **AsPOS Tagger**
- **Model:** [AsPOS Assamese POS Tagger](https://huggingface.co/dpathak/aspos_assamese_pos_tagger)
- **Developers:** Dhrubajyoti Pathak, Satyaki Nandi, Pranjal Sarmah
- **Paper:** [AsPOS: Assamese Part of Speech Tagger using Deep Learning Approach](https://arxiv.org/pdf/2212.07043)
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

### 🤖 **IndicBERT**
- **Model:** [IndicBERT by AI4Bharat](https://huggingface.co/ai4bharat/indic-bert)
- **Organization:** AI4Bharat, IIT Madras
- **Paper:** [AI4Bharat IndicNLP Suite](https://arxiv.org/abs/2005.00085)
- **License:** Apache License 2.0

---

### 🛠️ **Indic NLP Library**
- **Repo:** [Indic NLP Library](https://github.com/anoopkunchukuttan/indic_nlp_library)
- **Author:** Anoop Kunchukuttan
- **License:** Apache License 2.0

---

### 🧠 **Flair NLP Library**
- **Repo:** [Flair](https://github.com/flairNLP/flair)
- **Organization:** Zalando Research
- **License:** MIT License

---

### 📦 Other Libraries
- `transformers` by Hugging Face
-  `flask`, `torch`

---

> ⚠️ **Disclaimer:** All models and libraries are used strictly for academic, research, and educational purposes. Ownership and intellectual property rights belong to their respective authors and organizations.
