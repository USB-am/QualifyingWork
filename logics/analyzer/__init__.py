from urllib.parse import urlparse


def get_domain(url: str) -> str:
	return urlparse(url).netloc


class Analyzer:
	''' Предоставляет методы для анализа сайта '''
	title = 'title'
	metas = ['meta1', 'meta2']

	def __init__(self, url: str):
		self.url = url
		self.domain = urlparse(self.url).netloc

	def test_print(self):
		return 'test_print is worked!'