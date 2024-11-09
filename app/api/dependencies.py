from app.config import TextRules, MarginRules
from app.services.composite_analyzer import APACompositeAnalyzer
from app.services.components import (
    TitlePageAnalyzer,
    AbstractAnalyzer,
    KeywordsAnalyzer,
    MainTextAnalyzer,
    CitationsAnalyzer,
    ReferencesAnalyzer,
)
from app.services.general import MarginAnalyzer, HeaderAnalyzer, TextAnalyzer


def get_main_analyzer():
    return APACompositeAnalyzer(
        analyzers=[
            MarginAnalyzer(MarginRules.create()),
            HeaderAnalyzer(),
            TextAnalyzer(TextRules.create()),
            TitlePageAnalyzer(),
            AbstractAnalyzer(),
            KeywordsAnalyzer(),
            MainTextAnalyzer(),
            CitationsAnalyzer(),
            ReferencesAnalyzer(),
        ]
    )
