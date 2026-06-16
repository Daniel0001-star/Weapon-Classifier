from flask import Flask, render_template, request, jsonify
import joblib
import cv2
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")

IMG_SIZE = 64

def preprocess(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    return img.flatten()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["image"]
    path = "temp.jpg"
    file.save(path)

    img = preprocess(path)
    prediction = model.predict([img])[0]

    label = "Rifle" if prediction == 1 else "No Threat"

    return jsonify({"prediction": label})

    return jsonify({
    "prediction": label,
    "confidence": float(confidence)

if __name__ == "__main__":
    app.run(debug=True)
