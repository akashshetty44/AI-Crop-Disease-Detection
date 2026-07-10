import os
import numpy as np
from PIL import Image
import tensorflow as tf

# Load trained model
MODEL_PATH = "model/crop_model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Disease classes (must match training dataset order)
CLASS_NAMES = [
    "Apple Scab",
    "Apple Black Rot",
    "Apple Cedar Rust",
    "Healthy Apple",
    "Corn Common Rust",
    "Corn Gray Leaf Spot",
    "Healthy Corn",
    "Potato Early Blight",
    "Potato Late Blight",
    "Healthy Potato",
    "Tomato Early Blight",
    "Tomato Late Blight",
    "Tomato Leaf Mold",
    "Tomato Mosaic Virus",
    "Healthy Tomato"
]


def preprocess_image(image_path):
    """
    Load and preprocess image for prediction.
    """
    image = Image.open(image_path).convert("RGB")
    image = image.resize((224, 224))

    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    return image


def predict_disease(image_path):
    """
    Predict crop disease from uploaded leaf image.
    Returns:
        disease_name, confidence
    """

    if not os.path.exists(image_path):
        return "Image not found", 0.0

    image = preprocess_image(image_path)

    prediction = model.predict(image, verbose=0)

    class_index = np.argmax(prediction)
    confidence = float(np.max(prediction))

    disease = CLASS_NAMES[class_index]

    return disease, confidence
