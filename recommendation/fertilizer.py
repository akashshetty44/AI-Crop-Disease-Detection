# recommendation/fertilizer.py

# Disease-wise fertilizer and pesticide recommendations

RECOMMENDATIONS = {

    "Apple Scab": {
        "fertilizer": "NPK 20-20-20",
        "pesticide": "Mancozeb"
    },

    "Apple Black Rot": {
        "fertilizer": "Organic Compost + Potash",
        "pesticide": "Captan"
    },

    "Apple Cedar Rust": {
        "fertilizer": "Potassium Sulphate",
        "pesticide": "Myclobutanil"
    },

    "Healthy Apple": {
        "fertilizer": "Vermicompost",
        "pesticide": "No pesticide required"
    },

    "Corn Common Rust": {
        "fertilizer": "Nitrogen Rich Fertilizer",
        "pesticide": "Propiconazole"
    },

    "Corn Gray Leaf Spot": {
        "fertilizer": "Balanced NPK",
        "pesticide": "Azoxystrobin"
    },

    "Healthy Corn": {
        "fertilizer": "Organic Compost",
        "pesticide": "No pesticide required"
    },

    "Potato Early Blight": {
        "fertilizer": "NPK 19-19-19",
        "pesticide": "Mancozeb"
    },

    "Potato Late Blight": {
        "fertilizer": "Potassium Rich Fertilizer",
        "pesticide": "Metalaxyl"
    },

    "Healthy Potato": {
        "fertilizer": "Farmyard Manure",
        "pesticide": "No pesticide required"
    },

    "Tomato Early Blight": {
        "fertilizer": "NPK 19-19-19",
        "pesticide": "Chlorothalonil"
    },

    "Tomato Late Blight": {
        "fertilizer": "Calcium Nitrate",
        "pesticide": "Copper Oxychloride"
    },

    "Tomato Leaf Mold": {
        "fertilizer": "Balanced NPK",
        "pesticide": "Copper Fungicide"
    },

    "Tomato Mosaic Virus": {
        "fertilizer": "Micronutrient Mix",
        "pesticide": "Remove infected plants (no effective pesticide)"
    },

    "Healthy Tomato": {
        "fertilizer": "Organic Compost",
        "pesticide": "No pesticide required"
    }

}


def get_recommendation(disease):
    """
    Returns fertilizer and pesticide recommendation
    based on detected disease.
    """

    recommendation = RECOMMENDATIONS.get(
        disease,
        {
            "fertilizer": "Consult Agricultural Officer",
            "pesticide": "Consult Agricultural Officer"
        }
    )

    return (
        recommendation["fertilizer"],
        recommendation["pesticide"]
    )
