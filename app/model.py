import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

def load_model():
    model_path = os.path.join(os.path.dirname(__file__), '../model/sentiment_model.pkl')
    with open(model_path, 'rb') as f:
        return pickle.load(f)

def predict_sentiment(model, text):
    prediction = model.predict([text])[0]
    return prediction
