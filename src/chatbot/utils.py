import nltk
import spacy
import pickle

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    # Function to preprocess input text
    text = text.lower()
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

def tokenize_text(text):
    # Function to tokenize input text
    return nltk.word_tokenize(text)

def load_model(model_path):
    # Function to load the trained model
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def generate_response(input_text, model):
    # Function to generate a response from the model
    preprocessed_text = preprocess_text(input_text)
    response = model.predict([preprocessed_text])
    return response[0]

def save_model(model, model_path):
    # Function to save the trained model
    with open(model_path, 'wb') as file:
        pickle.dump(model, file)