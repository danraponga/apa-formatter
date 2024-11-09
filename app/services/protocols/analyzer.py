from typing import Protocol

from docx import Document

from app.models.issue import FormatIssue


class Analyzer(Protocol):
    def validate(self, doc: Document) -> list[FormatIssue]:
        raise NotImplementedError
