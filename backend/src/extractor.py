from utils.processing_functions import (
    pdf2img,
    img_processing,
    get_text,
)


def extact_info(file_path, doc_type):
    pages = pdf2img(file_path)
    for page in pages:
        img = img_processing(page)
        text = get_text(img)
        text = "\n" + text
        if doc_type == "prescription":
            return text
        elif doc_type == "patient_details":
            pass


if __name__ == "__main__":
    extact_info("../resources/prescription/pre_1.pdf", "prescription")
