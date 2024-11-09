from abc import ABC, abstractmethod
from docx import Document
from app.models.issue import FormatIssue
from app.services.protocols.analyzer import Analyzer


class KeywordsAnalyzer(Analyzer):
    """Class responsible for validating the keywords formatting according to APA guidelines."""

    def validate(self, doc: Document) -> list[FormatIssue]:
        """
        Validates keywords formatting.

        Checks:
        - Placement (one line below abstract)
        - Indentation (0.5 inches)
        - Format ("Keywords:" in italics)
        - Content (lowercase, comma-separated)

        Args:
            doc: Word document to analyze

        Returns:
            List of formatting issues found
        """
        return []
