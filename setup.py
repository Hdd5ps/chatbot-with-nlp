from setuptools import setup, find_packages

setup(
    name='chatbot_nlp',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'Flask',
        'nltk',
        'spacy',
        'pandas',
        'scikit-learn',
        'flask-cors',
        'joblib'
    ],
    entry_points={
        'console_scripts': [
            'train_chatbot=chatbot.train:train_chatbot',
        ],
    },
)