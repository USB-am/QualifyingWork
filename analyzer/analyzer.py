from parse import Page
from . import text as TextAnalyzer


def get_page_analyze(page: Page) -> dict:
	output = {
		'title_to_h1': TextAnalyzer.Correlation.text_text(page.title, page.h1),
		'title_to_request': TextAnalyzer.Correlation.text_list(
			page.title, page.keywords),	# KEYWORDS?
	}

	return output


class Analyzer:
	'''
	Представление анализа данных страницы.
	~params:
	: page: Page - разобранная информация о странице.
	'''

	def __init__(self, page: Page):
		self.page = page

		page_analyze = get_page_analyze(self.page)
		self.__dict__.update(page_analyze)

		# print(self.title_to_h1)
		print(self.title_to_request)