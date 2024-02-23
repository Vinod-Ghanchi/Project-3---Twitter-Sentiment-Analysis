from flask import Flask, render_template, request
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('sentiment_model.joblib')

# Load the TF-IDF vectorizer
vectorizer = joblib.load('tfidf_vectorizer.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']

        # Vectorize the input text
        text_vectorized = vectorizer.transform([text])

        # Make a prediction
        prediction = model.predict(text_vectorized)

        # Map the prediction to sentiment label
        sentiment_mapping = {0: 'Negative', 4: 'Positive'}
        result = sentiment_mapping[prediction[0]]

        return render_template('index.html', result=result, text=text)

if __name__ == '__main__':
    app.run(debug=True)
