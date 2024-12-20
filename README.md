# Chatbot NLP Project

This project implements a chatbot using Python and natural language processing (NLP) libraries such as NLTK and SpaCy. The chatbot is trained on a dataset of customer service interactions to improve response accuracy and is integrated with a web interface using Flask.

## Project Structure

```
chatbot-nlp
├── src
│   ├── app.py                # Entry point of the Flask application
│   ├── chatbot
│   │   ├── __init__.py       # Initializes the chatbot package
│   │   ├── model.py          # Defines the chatbot model architecture
│   │   ├── train.py          # Functions for training the chatbot model
│   │   └── utils.py          # Utility functions for the chatbot
│   ├── static
│   │   └── styles.css        # CSS styles for the web interface
│   └── templates
│       └── index.html        # HTML template for user interaction
├── data
│   └── customer_service_interactions.csv  # Dataset for training
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── config.py                 # Configuration settings for Flask
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd chatbot-nlp
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Prepare the dataset:
   Ensure that the `customer_service_interactions.csv` file is located in the `data` directory.

4. Run the application:
   ```
   python src/app.py
   ```

5. Access the chatbot interface:
   Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage

- Interact with the chatbot through the web interface.
- The chatbot will respond based on the training it received from the customer service interactions dataset.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.