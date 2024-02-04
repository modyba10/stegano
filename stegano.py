from PIL import Image
def text_to_binary(text):
    binary_string = ''.join(format(ord(char), '08b') for char in text)
    return binary_string


def load_image(image_path):
    img = Image.open(image_path)
    return img
