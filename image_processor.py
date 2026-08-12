from PIL import Image
import os

# Folder where image_processor.py is located
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Project-2 folder
PROJECT_DIR = os.path.dirname(CURRENT_DIR)


def load_image(image_name):
    """
    Loads an image from the Project-2/images folder.
    """

    image_path = os.path.join(PROJECT_DIR, "images", image_name)

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    return Image.open(image_path)


def get_image_info(image):
    """
    Returns basic information about the image.
    """

    return {
        "Width": image.width,
        "Height": image.height,
        "Mode": image.mode,
        "Format": image.format,
    }