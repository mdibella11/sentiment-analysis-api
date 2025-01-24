# Sentiment Analysis API

## Overview
This project implements a RESTful API for sentiment analysis. Given a piece of text as input, the API predicts the sentiment (positive, negative, or neutral) using a pre-trained machine learning model. This project was created and maintained by Marco Di Bella.

## Features
- RESTful endpoints for analyzing sentiment.
- Scikit-learn-based pre-trained model integration.
- Input validation and error handling.
- Easy Docker-based deployment.

## Installation

### Prerequisites
- Python 3.9+
- pip
- Docker (optional)

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/mdibella11/sentiment-analysis-api.git
   cd sentiment-analysis-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the API:
   ```bash
   python app/main.py
   ```

4. Access the API at `http://127.0.0.1:5000`.

### Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t sentiment-analysis-api .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 sentiment-analysis-api
   ```

## Endpoints
### `GET /`
Returns a welcome message.

### `POST /analyze`
Analyzes the sentiment of the given text.

#### Request Body
```json
{
  "text": "Your input text here."
}
```

#### Response
```json
{
  "text": "Your input text here.",
  "sentiment": "positive"
}
```

## Author
Marco Di Bella

## License
This project is licensed under the MIT License.
