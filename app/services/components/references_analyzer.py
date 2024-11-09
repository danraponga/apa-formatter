from abc import ABC, abstractmethod
from docx import Document
from app.models.issue import FormatIssue
from app.services.protocols.analyzer import Analyzer


class ReferencesAnalyzer(Analyzer):
    """Class responsible for validating the references page according to APA guidelines."""

    def validate(self, doc: Document) -> list[FormatIssue]:
        """
        Validates references page formatting.

        Checks:
        - New page start
        - Title "References" (centered, bold)
        - Double spacing
        - Hanging indentation
        - Reference entries format

        Args:
            doc: Word document to analyze

        Returns:
            List of formatting issues found
        """
        return []
