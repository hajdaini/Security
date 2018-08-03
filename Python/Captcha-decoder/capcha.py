"""
@Author : AJDAINI Hatim
@GitHub : https://github.com/Hajdaini
"""

from PIL import Image
import pytesseract
from sys import platform


def change_contrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast(c):
        return 128 + factor * (c - 128)

    return img.point(contrast)


def remove_gray_noise(image):
    colors = list(image.getdata())
    data = []
    for c in colors:
        if c < 10:
            data.append(0)
        else:
            data.append(255)
    image.putdata(data)

CAPTCHA_NAME = 'images/level5.png'  # put your image name here
RATIO = (116, 56)
ZOOM = 1.6  # change the zoom if the result is not correct
RESIZE_VALUE = (int(RATIO[0] * ZOOM), int(RATIO[1] * ZOOM))
CONTRAST = 200


# Manipulation of the the upload image
image = Image.open(CAPTCHA_NAME)
image = image.convert('L')  # grayscale
image = image.resize(RESIZE_VALUE)
image = change_contrast(image, CONTRAST)
remove_gray_noise(image)

# image.show()  #uncomment this line if you want to see the result of the image upload

"""
if you are in windows then donwload tesseract from https://github.com/UB-Mannheim/tesseract/wiki 
and put your absolute path of tesseract.exe like i did
"""
if platform == "win32":
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

print(pytesseract.image_to_string(image))
