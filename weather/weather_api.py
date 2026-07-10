import requests
from config import WEATHER_API_KEY, DEFAULT_CITY


def get_weather(city=DEFAULT_CITY):
    """
    Fetch current weather details using OpenWeatherMap API.
    Returns a dictionary containing weather information.
    """

    if WEATHER_API_KEY == "YOUR_OPENWEATHER_API_KEY":
        return {
            "city": city,
            "temperature": "N/A",
            "humidity": "N/A",
            "description": "API key not configured"
        }

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={WEATHER_API_KEY}"
        f"&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()

            return {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"].title()
            }

        return {
            "city": city,
            "temperature": "N/A",
            "humidity": "N/A",
            "description": "Weather unavailable"
        }

    except Exception:
        return {
            "city": city,
            "temperature": "N/A",
            "humidity": "N/A",
            "description": "Connection error"
        }
