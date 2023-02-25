from fastapi import FastAPI, UploadFile, Form, File
import uvicorn
from uuid import uuid4
import os
from extractor import extact_info
from enum import Enum

app = FastAPI()

supported_file_formats = [
    ".jpg",
    ".jpeg",
    ".png",
    ".pbm",
    ".pgm",
    ".ppm",
    ".pxm",
    ".pnm",
    ".pdf",
]


class allowed_document_types(str, Enum):
    prescription = "prescription"
    patient_details = "patient_details"


@app.post("/extract")
async def extract(
    document_type: allowed_document_types = Form(...),
    file: UploadFile = File(...),
):
    file_content = file.file.read()
    filename = file.filename
    file_extension = ""

    for file_format in supported_file_formats:
        if filename.endswith(file_format):
            file_extension = f"{file_format}"
            break

    file_path = f"./{str(uuid4())}{file_extension}"

    with open(file_path, "wb") as f:
        f.write(file_content)

    try:
        data = extact_info(file_path, document_type)
    except Exception as e:
        data = {"error": str(e)}

    if os.path.exists(file_path):
        os.remove(file_path)
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
