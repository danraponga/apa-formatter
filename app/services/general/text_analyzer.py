from docx import Document
from app.config import TextRules
from app.models.issue import FormatIssue, IssuePosition, IssueType
from app.services.protocols.analyzer import Analyzer


class TextAnalyzer(Analyzer):
    def __init__(self, rules: TextRules) -> None:
        self.rules = rules

    def validate(self, doc: Document) -> list[FormatIssue]:
        issues = []

        for i, paragraph in enumerate(doc.paragraphs):
            current_spacing = paragraph.paragraph_format.line_spacing
            if current_spacing != self.rules.line_spacing:
                issues.append(
                    FormatIssue(
                        position=IssuePosition(paragraph_index=i),
                        issue_type=IssueType.LINE_SPACING,
                        current_value=str(current_spacing)
                        if current_spacing
                        else "missing",
                        suggested_value=str(self.rules.line_spacing),
                        description="Incorrect line spacing",
                    )
                )
            if (
                paragraph.paragraph_format.space_before
                or paragraph.paragraph_format.space_after
            ):
                issues.append(
                    FormatIssue(
                        position=IssuePosition(paragraph_index=i),
                        issue_type=IssueType.PARAGRAPH_SPACING,
                        current_value="extra spacing present",
                        description="Extra spacing between paragraphs is not allowed",
                    )
                )

            current_offset = 0
            for run in paragraph.runs:
                run_length = len(run.text)

                if run.font.name and run.font.name != self.rules.font.name:
                    issues.append(
                        FormatIssue(
                            position=IssuePosition(
                                paragraph_index=i,
                                start_offset=current_offset,
                                end_offset=current_offset + run_length,
                            ),
                            issue_type=IssueType.FONT,
                            current_value=run.font.name,
                            suggested_value=self.rules.font.name,
                            description="Incorrect font used",
                        )
                    )

                if run.font.size and run.font.size.pt != self.rules.font.size:
                    issues.append(
                        FormatIssue(
                            position=IssuePosition(
                                paragraph_index=i,
                                start_offset=current_offset,
                                end_offset=current_offset + run_length,
                            ),
                            issue_type=IssueType.FONT,
                            current_value=str(run.font.size.pt),
                            suggested_value=str(self.rules.font.size),
                            description="Incorrect font size",
                        )
                    )
                current_offset += run_length

        return issues
