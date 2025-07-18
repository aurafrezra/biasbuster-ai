### ✅ Updated `app.py`

from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']

    # Dummy analysis
    biases = ["Gender Bias", "Racial Bias", "Political Bias", "Age Bias", "Cultural Bias"]
    scores = [random.randint(5, 60) for _ in biases]

    return render_template(
        'result.html',
        results=zip(biases, scores),
        labels=biases,
        scores=scores
    )

if __name__ == '__main__':
    app.run(debug=True)

