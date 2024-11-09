from fastapi import APIRouter, Depends, HTTPException
from fastapi import UploadFile, File

from app.api.dependencies import get_main_analyzer
from app.models.issue import FormatIssue
from app.services.composite_analyzer import APACompositeAnalyzer
from app.utils.test_document import create_test_document
from app.utils.convert_file import convert_file_to_document


api_router = APIRouter(prefix="/api")


@api_router.post("/validate")
def validate_document(
    file: UploadFile = File(),
    analyzer: APACompositeAnalyzer = Depends(get_main_analyzer),
) -> list[FormatIssue]:
    if not file.filename.endswith(".docx"):
        raise HTTPException(status_code=400, detail="Only .docx file are supported")

    try:
        doc = convert_file_to_document(file)
        return analyzer.validate(doc)
    except Exception:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")


@api_router.post("/mock/validate")
def validate_test_document(
    analyzer: APACompositeAnalyzer = Depends(get_main_analyzer),
) -> list[FormatIssue]:
    doc = create_test_document()
    return analyzer.validate(doc)
