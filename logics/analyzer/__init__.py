from urllib.parse import urlparse

from logics.parsers import WebPage


def get_domain(url: str) -> str:
	return urlparse(url).netloc


class Analyzer:
	''' Предоставляет методы для анализа сайта '''

	def __init__(self, url: str):
		self.url = f'https://{url}'
		self.domain = get_domain(self.url)

		self.web_page = WebPage(self.url)
		web_page_data = self.web_page.get_data()
		self.__dict__.update(web_page_data)

	def __str__(self):
		return f'{self.domain} - {self.title.text}'