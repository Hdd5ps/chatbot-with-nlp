import pandas as pd
import spacy
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import joblib

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    nlp = spacy.load("en_core_web_sm")
    processed_data = []
    for text in data['text']:
        doc = nlp(text)
        tokens = [token.lemma_ for token in doc if not token.is_stop]
        processed_data.append(" ".join(tokens))
    return processed_data

def train_model(processed_data, labels):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(processed_data)
    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)
    
    model = MultinomialNB()
    model.fit(X_train, y_train)
    
    joblib.dump(model, 'chatbot_model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')

def main():
    data = load_data('../data/customer_service_interactions.csv')
    processed_data = preprocess_data(data)
    labels = data['label']
    train_model(processed_data, labels)

if __name__ == "__main__":
    main()