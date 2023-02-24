from src.document_parsers.patient_details_parser import PatientDetailsParser
from src.document_parsers.prescription_parser import PrescriptionParser

from utils.processing_functions import (
    pdf2img,
    img_processing,
    get_text,
)


def extact_info(file_path, doc_type):
    pages = pdf2img(file_path)
    document_text = ""
    for page in pages:
        img = img_processing(page)
        text = get_text(img)
        document_text = document_text + "\n" + text
    if doc_type == "prescription":
        data = PrescriptionParser(document_text).parse()
    elif doc_type == "patient_details":
        print(PatientDetailsParser(document_text).data.keys())
        data = PatientDetailsParser(document_text).parse()
    else:
        raise Exception("Invalid document type")
    return data


if __name__ == "__main__":
    # extact_info("./pd_1.pdf", "patient_details")
    print(extact_info("./pre_2.pdf", "prescription"))
