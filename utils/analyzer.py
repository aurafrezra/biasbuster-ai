from transformers import pipeline
import re

sentiment_model = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")
bias_keywords = {
    "left-wing": "left",
    "right-wing": "right",
    "liberal": "left",
    "conservative": "right",
    "propaganda": "extreme",
    "fake": "extreme",
    "biased": "extreme"
}

def highlight_bias(text):
    highlighted = text
    for word in bias_keywords:
        pattern = re.compile(rf'\b{word}\b', flags=re.IGNORECASE)
        highlighted = pattern.sub(f'<mark class="bias">{word}</mark>', highlighted)
    return highlighted

def analyze_text(text):
    sentiment = sentiment_model(text)[0]
    bias_score = sum(text.lower().count(word) for word in bias_keywords) * 10
    bias_level = "Neutral" if bias_score < 20 else "Biased"
    highlighted_text = highlight_bias(text)

    left_bias = sum(1 for k in ["left-wing", "liberal"] if k in text.lower())
    right_bias = sum(1 for k in ["right-wing", "conservative"] if k in text.lower())

    return {
        "sentiment": sentiment,
        "bias_score": bias_score,
        "bias_level": bias_level,
        "highlighted": highlighted_text,
        "bias_graph": {"left": left_bias, "right": right_bias}
    }
