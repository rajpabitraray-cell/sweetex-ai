# ================================
# Sweetex AI — Live Signal Server
# Python Flask Backend
# ================================

# INSTALL:
# pip install flask flask-cors pillow pytesseract numpy

import os
import random
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import pytesseract

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
CORS(app)

MARKETS = [
    "EUR/USD", "GBP/USD", "USD/JPY", "USD/CHF",
    "AUD/USD", "NZD/USD", "USD/CAD",
    "EUR/JPY", "GBP/JPY", "AUD/JPY", "CHF/JPY",
    "USD/INR (OTC)", "EUR/BRL (OTC)", "GBP/PKR (OTC)",
    "BTC/USD", "ETH/USD", "SOL/USD",
    "NASDAQ", "S&P 500", "DOW JONES"
]

PATTERNS = [
    "Three White Soldiers",
    "Engulfing",
    "Doji Reversal",
    "Breakout",
    "Liquidity Grab",
    "CHoCH",
    "BOS"
]

def fake_ai_engine():
    trend = random.choice(["Up", "Down"])
    signal = "CALL" if trend == "Up" else "PUT"
    return {
        "pair": random.choice(MARKETS),
        "trend": trend,
        "signal": signal,
        "tf": random.choice(["M1", "M5", "M15"]),
        "pattern": random.choice(PATTERNS),
        "support": round(random.uniform(1.0000, 100.0000), 4),
        "resistance": round(random.uniform(1.0000, 100.0000), 4)
    }

@app.route("/analyze", methods=["POST"])
def analyze():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image_file = request.files["image"]
    path = os.path.join(UPLOAD_FOLDER, image_file.filename)
    image_file.save(path)

    try:
        img = Image.open(path)
        extracted_text = pytesseract.image_to_string(img)
    except:
        extracted_text = ""

    ai_result = fake_ai_engine()
    ai_result["ocr_text"] = extracted_text[:300]
    return jsonify(ai_result)

if __name__ == "__main__":
    print("Sweetex AI Server Running on port 5000")
    app.run(host="0.0.0.0", port=5000)
