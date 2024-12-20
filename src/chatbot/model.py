from nltk.chat.util import Chat, reflections
import spacy
import json

class ChatbotModel:
    def __init__(self, intents_file):
        self.intents = self.load_intents(intents_file)
        self.nlp = spacy.load("en_core_web_sm")
        self.chatbot = self.create_chatbot()

    def load_intents(self, file_path):
        with open(file_path) as file:
            return json.load(file)

    def create_chatbot(self):
        pairs = []
        for intent in self.intents['intents']:
            for pattern in intent['patterns']:
                pairs.append((pattern, intent['responses']))
        return Chat(pairs, reflections)

    def get_response(self, user_input):
        response = self.chatbot.respond(user_input)
        if response is None:
            return "I'm sorry, I don't understand that. Can you please rephrase?"
        return response

    def process_input(self, user_input):
        doc = self.nlp(user_input)
        return " ".join([token.lemma_ for token in doc])  # Lemmatization as an example

    def chat(self, user_input):
        processed_input = self.process_input(user_input)
        return self.get_response(processed_input)