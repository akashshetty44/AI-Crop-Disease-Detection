# 🌿 AI Crop Disease Detection

An AI-powered web application that detects crop diseases from leaf images using Deep Learning and provides fertilizer, pesticide, and weather-based recommendations.

---

## Features

- Upload crop leaf images
- AI-based disease detection
- Confidence score
- Fertilizer recommendation
- Pesticide recommendation
- Weather integration
- SQLite database for prediction history
- Responsive web interface

---

## Technologies Used

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Flask (Python)

### AI/ML
- TensorFlow
- Keras
- OpenCV
- NumPy

### Database
- SQLite

### API
- OpenWeatherMap API

---

## Project Structure

AI_Crop_Disease_Detection/

├── app.py

├── config.py

├── requirements.txt

├── README.md

├── dataset/

├── database/

│ └── database.py

├── model/

│ ├── train.py

│ ├── predict.py

│ └── crop_model.h5

├── recommendation/

│ └── fertilizer.py

├── weather/

│ └── weather_api.py

├── utils/

│ └── preprocess.py

├── templates/

│ ├── index.html

│ └── result.html

├── static/

│ ├── css/style.css

│ ├── js/script.js

│ └── uploads/

---

## Installation

Clone the project

```bash
git clone https://github.com/yourusername/AI_Crop_Disease_Detection.git
cd AI_Crop_Disease_Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Dataset

Download the PlantVillage dataset and extract it into the `dataset/` folder.

Example:

```
dataset/
├── Tomato___Early_blight/
├── Tomato___Late_blight/
├── Potato___Early_blight/
├── Potato___Late_blight/
├── Apple___Apple_scab/
└── ...
```

---

## Train the Model

```bash
python model/train.py
```

The trained model will be saved as:

```
model/crop_model.h5
```

---

## Weather API

Create a free API key from OpenWeatherMap.

Open `config.py` and replace:

```python
WEATHER_API_KEY = "YOUR_OPENWEATHER_API_KEY"
```

with your API key.

---

## Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## How It Works

1. Upload a crop leaf image.
2. The AI model predicts the disease.
3. The confidence score is displayed.
4. Fertilizer and pesticide recommendations are generated.
5. Current weather is fetched from the Weather API.
6. The prediction is saved to the SQLite database.

---

## Future Enhancements

- Live camera detection
- Mobile application
- Multi-language support
- GPS-based crop advice
- Drone image support
- TensorFlow Lite offline prediction

---

## License

This project is intended for educational and academic purposes.

---

## Author

Akash B R
Final Year Engineering Project
AI Crop Disease Detection
