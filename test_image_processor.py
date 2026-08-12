from image_processor import load_image, get_image_info

image = load_image("aira.png")

info = get_image_info(image)

print(info)