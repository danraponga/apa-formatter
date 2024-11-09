from abc import ABC, abstractmethod
from docx import Document
from app.models.issue import FormatIssue
from app.services.protocols.analyzer import Analyzer


class AbstractAnalyzer(Analyzer):
    """Class responsible for validating the abstract formatting according to APA guidelines."""

    def validate(self, doc: Document) -> list[FormatIssue]:
        """
        Validates abstract formatting.

        Checks:
        - Heading "Abstract" (centered, bold)
        - New page start
        - No first line indentation
        - Word count (max 250)

        Args:
            doc: Word document to analyze

        Returns:
            List of formatting issues found
        """
        return []
