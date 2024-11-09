from dataclasses import dataclass
from enum import Enum


@dataclass
class IssuePosition:
    paragraph_index: int | None = None
    section_index: int | None = None
    start_offset: int | None = None
    end_offset: int | None = None


class IssueType(Enum):
    MARGIN = "margin"
    HEADER = "header"
    LINE_SPACING = "line_spacing"
    PARAGRAPH_SPACING = "paragraph_spacing"
    FONT = "font"
    SECTION = "section"


@dataclass
class FormatIssue:
    position: IssuePosition
    description: str
    issue_type: IssueType
    current_value: str
    suggested_value: str | None = None
