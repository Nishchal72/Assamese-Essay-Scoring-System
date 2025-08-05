from flair.models import SequenceTagger
from transformers import AutoTokenizer, AutoModel
import os


model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "AsPOS.pt"))
flair_tagger = SequenceTagger.load(model_path)

# Load IndicBERT tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("ai4bharat/indic-bert")
indicbert_model = AutoModel.from_pretrained("ai4bharat/indic-bert")
