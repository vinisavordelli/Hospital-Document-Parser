import numpy as np
import cv2
from pdf2image import convert_from_path
from pytesseract import image_to_string as img_2_str
import re

pdf_test_file = "../resources/prescription/pre_1.pdf"


def convert_pdf_to_images(pdf_path):
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


sample_text = get_text(img_processing(convert_pdf_to_images(pdf_test_file)[0]))


def get_info_from_text(pattern, text, flags=0):
    return re.findall(pattern, text, flags)[0].strip()


def info_to_dict(text):
    return {
        "Doctor Info": get_info_from_text("Dr(.*)Name", text, re.DOTALL),
        "Patient Name": get_info_from_text("Name:(.*)Date", text),
        "Address": get_info_from_text("Address[^\n]", text),
        "Prescription": get_info_from_text(
            "Address[^\n]*(.*)Directions", text, flags=re.DOTALL
        ),
        "Directions": get_info_from_text(
            "Directions:(.*)Refill", text, flags=re.DOTALL
        ),
        "Refill": get_info_from_text("Refill:(.*)", text),
    }


print(sample_text)
print(info_to_dict(sample_text))
