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

        document_text = "\n" + text
        if doc_type == "prescription":
            print(document_text)
            return document_text
        elif doc_type == "patient_details":
            pass


if __name__ == "__main__":
    extact_info("./pd_1.pdf", "prescription")
