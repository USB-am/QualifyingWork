from dataclasses import dataclass

from logics.tools import Request
from logics import parser as Parser


@dataclass
class TextAnalyzer:
	'''
	Хранит информацию об анализе страницы.
	~params:
	clean: bool - наличие чистого (или наиболее близкого) вхождения запроса;
	keyword_density: float - плотность ключевых слов;
	'''

	clean: bool
	keyword_density: float


def analyze_text(text: str, keywords: list) -> TextAnalyzer:
	return TextAnalyzer(clean=True, keyword_density=1.0)