from parse import Page
from . import text as TextAnalyzer
from . import html as HTMLAnalyzer
from req import Request


def get_page_analyze(page: Page, request: Request) -> dict:
	output = {
		'title_to_h1': TextAnalyzer.Correlation.text_text(
			page.title, page.h1),
		'title_to_req': TextAnalyzer.Correlation.text_text(
			page.title, request.text),
		'req_in_text': int(TextAnalyzer.text_in_text(
			request.text, page.text)),
		'req_words_count': TextAnalyzer.compare_keywords_count(
			page, request),
		'req_in_20text': int(TextAnalyzer.text_in_text(
			request.text, TextAnalyzer._get_text_percent(page.text, 20))),
		'keywords_description': TextAnalyzer.Correlation.text_list(
			page.description, request.words),
		'has_list_or_table': int(HTMLAnalyzer.has_tags(
			page, 'ol', 'ul', 'table')),
		'req_in_h': TextAnalyzer.request_in_captions(
			request.text, page.captions),
		'imgs_number': int(HTMLAnalyzer.imgs_number_in_text(
			page.text, page.imgs)),
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

		self.attrs = get_page_analyze(self.page, self.request)

	def __str__(self):
		return f'<Analyzer "{self.page.url}">'