import os

# Base Directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Upload Folder
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")

# SQLite Database
DATABASE = os.path.join(BASE_DIR, "database", "crop_disease.db")

# Trained AI Model
MODEL_PATH = os.path.join(BASE_DIR, "model", "crop_model.h5")

# Image Settings
IMAGE_SIZE = (224, 224)

# Flask Secret Key
SECRET_KEY = "crop_disease_detection_secret_key"

# OpenWeatherMap API Key
# Replace with your own API key from:
# https://openweathermap.org/api
WEATHER_API_KEY = "YOUR_OPENWEATHER_API_KEY"

# Default City
DEFAULT_CITY = "Bengaluru"

# Allowed Image Extensions
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

# Disease Classes (PlantVillage Dataset)
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
