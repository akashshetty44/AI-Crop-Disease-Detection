from flask import Flask, render_template, request
import os

from model.predict import predict_disease
from recommendation.fertilizer import get_recommendation
from weather.weather_api import get_weather
from database.database import init_db, save_prediction

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize database
init_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    if "leaf_image" not in request.files:
        return "No image uploaded"

    image = request.files["leaf_image"]

    if image.filename == "":
        return "Please select an image"

    image_path = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
    image.save(image_path)

    # AI Prediction
    disease, confidence = predict_disease(image_path)

    # Fertilizer Recommendation
    fertilizer, pesticide = get_recommendation(disease)

    # Weather (change city later or use GPS)
    weather = get_weather("Bengaluru")

    # Save to database
    save_prediction(
        image.filename,
        disease,
        confidence,
        fertilizer,
        pesticide
    )

    return render_template(
        "result.html",
        image=image.filename,
        disease=disease,
        confidence=round(confidence * 100, 2),
        fertilizer=fertilizer,
        pesticide=pesticide,
        weather=weather
    )


if __name__ == "__main__":
    app.run(debug=True)
