import numpy as np
from PIL import Image


IMAGE_SIZE = (224, 224)


def load_image(image_path):
    """
    Load image and convert to RGB.
    """
    image = Image.open(image_path).convert("RGB")
    return image


def resize_image(image):
    """
    Resize image to model input size.
    """
    return image.resize(IMAGE_SIZE)


def normalize_image(image):
    """
    Convert image to NumPy array and normalize pixel values.
    """
    image = np.array(image, dtype=np.float32)
    image = image / 255.0
    return image


def preprocess_image(image_path):
    """
    Complete preprocessing pipeline.
    Returns a NumPy array ready for prediction.
    """
    image = load_image(image_path)
    image = resize_image(image)
    image = normalize_image(image)

    # Add batch dimension
    image = np.expand_dims(image, axis=0)

    return image


if __name__ == "__main__":
    image_path = "sample_leaf.jpg"

    try:
        processed = preprocess_image(image_path)
        print("Image shape:", processed.shape)
        print("Image preprocessing successful!")
    except Exception as e:
        print("Error:", e)
