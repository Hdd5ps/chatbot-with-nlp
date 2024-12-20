from flask import Flask, request, jsonify, render_template
from chatbot.model import ChatbotModel
from chatbot.utils import preprocess_input

app = Flask(__name__)
chatbot = ChatbotModel()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    processed_input = preprocess_input(user_input)
    response = chatbot.generate_response(processed_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)