from parse import Page
from . import text as TextAnalyzer
from req import Request


def get_page_analyze(page: Page, request: Request) -> dict:
	output = {
		'title_to_h1': TextAnalyzer.Correlation.text_text(
			page.title, page.h1),
		'title_to_req': TextAnalyzer.Correlation.text_text(
			page.title, request.text),
		'req_in_text': int(TextAnalyzer.text_in_text(
			request.text, page.text)),
	}

	return output


class Analyzer:
	'''
	Представление анализа данных страницы.
	~params:
	: page: Page - разобранная информация о странице.
	'''

	def __init__(self, page: Page, request: Request):
		self.page = page
		self.request = request

		page_analyze = get_page_analyze(self.page, self.request)
		self.__dict__.update(page_analyze)
		self.relevance = 80
		print(self.req_in_text)

	def __str__(self):
		return f'<Analyzer "{self.page.url}" {self.relevance}%>'