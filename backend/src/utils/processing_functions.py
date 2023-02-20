from pdf2image import convert_from_path
import numpy as np
import cv2
from pytesseract import image_to_string as img_2_str


def pdf2img(pdf_path):
    images = convert_from_path(pdf_path)
    return images


def img_processing(img):
    b_w_img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    resized_img = cv2.resize(
        b_w_img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR
    )
    img = cv2.adaptiveThreshold(
        resized_img,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        71,
        11,
    )
    return img


def get_text(img):
    text = img_2_str(img, lang="eng")
    text = "\n" + text
    return text
