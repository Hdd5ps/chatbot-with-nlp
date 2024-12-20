class Config:
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'your_secret_key_here'
    DATABASE_URI = 'sqlite:///chatbot.db'
    NLP_MODEL = 'en_core_web_sm'  # SpaCy model
    NLTK_DATA_PATH = '/path/to/nltk_data'  # Update with your NLTK data path
    CUSTOMER_SERVICE_DATA_PATH = 'data/customer_service_interactions.csv'