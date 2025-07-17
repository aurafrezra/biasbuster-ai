from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)
classifier = pipeline("text-classification", model="facebook/bart-large-mnli")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    user_text = request.form.get('user_text', '').strip()
    if not user_text:
        return render_template('result.html', left_bias=0, right_bias=0)

    # Dummy logic — replace with real NLP logic later
    left_bias = 65
    right_bias = 35

    return render_template(
        'result.html',
        left_bias=left_bias,
        right_bias=right_bias
    )

    result = classifier(user_text)[0]
    label = result['label']
    score = result['score']

    return render_template('result.html', result=f"Prediction: {label}, Confidence: {score:.2f}")

if __name__ == '__main__':
    app.run(debug=True)
