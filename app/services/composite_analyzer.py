from docx import Document

from app.models.issue import FormatIssue
from app.services.protocols.analyzer import Analyzer


class APACompositeAnalyzer(Analyzer):
    """Main analyzer coordinating basic rules and component-specific validation."""

    def __init__(self, analyzers: list[Analyzer]) -> None:
        self.analyzers = analyzers

    def validate(self, doc: Document) -> list[FormatIssue]:
        issues = []

        for analyzer in self.analyzers:
            issues.extend(analyzer.validate(doc))

        return issues
