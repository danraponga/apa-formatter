from dataclasses import dataclass


@dataclass(frozen=True)
class FontRules:
    name: str
    size: float


@dataclass(frozen=True)
class TextRules:
    font: FontRules
    line_spacing: float

    @staticmethod
    def create() -> "TextRules":
        return TextRules(
            font=FontRules(name="Times New Roman", size=12.0),
            line_spacing=2.0,
        )


@dataclass(frozen=True)
class MarginRules:
    size: float

    @staticmethod
    def create() -> "MarginRules":
        return MarginRules(size=1.0)
