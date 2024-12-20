import pandas as pd
import spacy
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import joblib
import os

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    # Assuming the CSV has 'query' and 'response' columns
    queries = data['query'].tolist()
    responses = data['response'].tolist()
    return queries, responses

def train_model(queries, responses):
    # Convert queries to feature vectors
    X = [nlp(query).vector for query in queries]
    y = responses

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Gaussian Naive Bayes classifier
    model = GaussianNB()
    model.fit(X_train, y_train)

    # Save the trained model
    joblib.dump(model, 'chatbot_model.pkl')

def train_chatbot(data_path):
    queries, responses = preprocess_data(data_path)
    train_model(queries, responses)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, '..', 'data', 'customer_service_interactions.csv')
    print(f"Data path: {data_path}")
    if not os.path.exists(data_path):
        print(f"File not found: {data_path}")
    else:
        train_chatbot(data_path)