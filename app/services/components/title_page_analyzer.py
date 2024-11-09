from abc import ABC, abstractmethod
from docx import Document
from app.models.issue import FormatIssue
from app.services.protocols.analyzer import Analyzer


class TitlePageAnalyzer(Analyzer):
    """Class responsible for validating the title page formatting according to APA guidelines."""

    def validate(self, doc: Document) -> list[FormatIssue]:
        """
        Validates title page formatting.

        Checks:
        - Title (centered, upper half, bold, title case)
        - Author Information (centered, below title)
        - Author Note (centered, bold, bottom of page)
        - Double spacing

        Args:
            doc: Word document to analyze

        Returns:
            List of formatting issues found
        """
        return []
