from flask import Flask, request, jsonify, render_template
from chatbot.model import ChatbotModel
import os

app = Flask(__name__)

# Construct the correct path to the intents file
base_dir = os.path.dirname(os.path.abspath(__file__))
intents_path = os.path.join(base_dir, 'data', 'intents.json')

chatbot = ChatbotModel(intents_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chatbot.get_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)