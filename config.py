import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    MODEL_PATH = os.environ.get('MODEL_PATH') or 'path/to/your/model'
    DATA_PATH = os.environ.get('DATA_PATH') or 'data/customer_service_interactions.csv'
    NLTK_DATA_PATH = os.environ.get('NLTK_DATA_PATH') or 'path/to/nltk_data'
    SPACY_MODEL = os.environ.get('SPACY_MODEL') or 'en_core_web_sm'