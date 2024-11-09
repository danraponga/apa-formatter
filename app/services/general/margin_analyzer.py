from docx import Document
from app.config import MarginRules
from app.models.issue import FormatIssue, IssuePosition, IssueType
from app.services.protocols.analyzer import Analyzer


class MarginAnalyzer(Analyzer):
    def __init__(self, rules: MarginRules) -> None:
        self.rules = rules

    def validate(self, doc: Document) -> list[FormatIssue]:
        issues = []

        for section_index, section in enumerate(doc.sections):
            margins = [
                ("top", section.top_margin.inches),
                ("bottom", section.bottom_margin.inches),
                ("left", section.left_margin.inches),
                ("right", section.right_margin.inches),
            ]

            for margin_name, margin_value in margins:
                if margin_value != self.rules.size:
                    issues.append(
                        FormatIssue(
                            position=IssuePosition(section_index=section_index),
                            issue_type=IssueType.MARGIN,
                            current_value=f"{margin_value:.1f}",
                            suggested_value=str(self.rules.size),
                            description=f"Incorrect {margin_name} margin size",
                        )
                    )

        return issues
