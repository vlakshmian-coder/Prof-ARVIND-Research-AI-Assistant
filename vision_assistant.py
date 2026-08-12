from image_processor import load_image, get_image_info


def analyse_image(image_name):
    """
    Loads an image and returns a readable description.
    """

    image = load_image(image_name)

    info = get_image_info(image)

    result = f"""
Vision Analysis Complete

Image Name : {image_name}
Width      : {info['Width']} pixels
Height     : {info['Height']} pixels
Mode        : {info['Mode']}
Format      : {info['Format']}
"""

    return result