from flask import Flask, request, jsonify
from app.model import load_model, predict_sentiment

app = Flask(__name__)

model = load_model()

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Sentiment Analysis API!"})

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    try:
        data = request.get_json()
        text = data.get("text", None)
        if not text:
            return jsonify({"error": "No text provided."}), 400

        sentiment = predict_sentiment(model, text)
        return jsonify({"text": text, "sentiment": sentiment})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
