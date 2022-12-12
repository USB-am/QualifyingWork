from urllib.parse import urlparse

from fuzzywuzzy import fuzz

from logics.parsers import WebPage


def get_domain(url: str) -> str:
	return urlparse(url).netloc


def matching_text(comparable_text: str, text: str) -> float:
	return fuzz.partial_ratio(comparable_text, text)


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

	def get_tags_matching(self) -> float:
		# return matching_text()
		# print(self.title)
		# print(sorted(self.text)[0])
		return '123'

	def first_20_text(self) -> str:
		txt = self.all_text.first_text_percent(20)
		print(f'Text="{txt}"')

		return txt