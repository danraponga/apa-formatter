from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH

from app.models.issue import FormatIssue, IssuePosition, IssueType
from app.services.protocols.analyzer import Analyzer


class HeaderAnalyzer(Analyzer):
    def validate(self, doc: Document) -> list[FormatIssue]:
        issues = []

        for index, section in enumerate(doc.sections):
            if not section.header or not section.header.paragraphs:
                issues.append(
                    FormatIssue(
                        position=IssuePosition(section_index=index),
                        issue_type=IssueType.HEADER,
                        current_value="missing",
                        description="Header is empty. It should contain running head and page number",
                    )
                )
                return

            has_running_head = False
            has_page_number = False

            for i, paragraph in enumerate(section.header.paragraphs):
                if paragraph.alignment == WD_ALIGN_PARAGRAPH.LEFT:
                    text = paragraph.text.strip()
                    if not text.isupper():
                        issues.append(
                            FormatIssue(
                                position=IssuePosition(
                                    section_index=index,
                                    paragraph_index=i,
                                    start_offset=0,
                                    end_offset=len(text),
                                ),
                                issue_type=IssueType.HEADER,
                                current_value=text,
                                suggested_value=text.upper(),
                                description="Running head should be in all capitals",
                            )
                        )
                    has_running_head = True

                if paragraph.alignment == WD_ALIGN_PARAGRAPH.RIGHT:
                    has_page_number = True

            if not has_running_head:
                issues.append(
                    FormatIssue(
                        position=IssuePosition(section_index=index),
                        issue_type=IssueType.HEADER,
                        current_value="missing",
                        description="Missing running head in the header",
                    )
                )
            if not has_page_number:
                issues.append(
                    FormatIssue(
                        position=IssuePosition(section_index=index),
                        issue_type=IssueType.HEADER,
                        current_value="missing",
                        description="Missing right-aligned page number in the header",
                    )
                )

        return issues
