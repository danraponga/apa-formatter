from io import BytesIO
from docx import Document
from fastapi import UploadFile


def convert_file_to_document(file: UploadFile) -> Document:
    content = file.file.read()
    bytes_content = BytesIO(content)
    return Document(bytes_content)
