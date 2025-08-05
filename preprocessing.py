import re
from indicnlp import common
from indicnlp.normalize.indic_normalize import IndicNormalizerFactory

INDIC_RESOURCES_PATH = "./data/indic_nlp_resources"
common.set_resources_path(INDIC_RESOURCES_PATH)

normalizer_factory = IndicNormalizerFactory()
normalizer = normalizer_factory.get_normalizer("as")  # Assamese

def preprocess_text(text):
    return re.sub(r'\s+', ' ', text).strip()

def normalize_text(text):
    return " ".join([normalizer.normalize(w) for w in text.strip().split()])
