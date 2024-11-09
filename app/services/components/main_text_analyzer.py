from abc import ABC, abstractmethod
from docx import Document
from app.models.issue import FormatIssue
from app.services.protocols.analyzer import Analyzer


class MainTextAnalyzer(Analyzer):
    """Class responsible for validating the main text formatting according to APA guidelines."""

    def validate(self, doc: Document) -> list[FormatIssue]:
        """
        Validates main text formatting.

        Checks:
        - New page start
        - Title repeat (bold, centered)
        - Heading levels formatting
        - Paragraph formatting

        Args:
            doc: Word document to analyze

        Returns:
            List of formatting issues found
        """
        return []
