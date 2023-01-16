import string
from typing import Union

import requests
from bs4 import BeautifulSoup as bs
from bs4 import element

from logics.parser import text as TextParser


def delete_punctuation_symbols(text: str) -> str:
	maketrans_text = str.maketrans('', '', string.punctuation)
	translated_text = text.translate(maketrans_text)

	return translated_text


def get_percent_text(text: str, percent: Union[float, int]) -> str:
	text_length = len(text)
	index = int(text_length * percent / 100)

	return text[:index]


class TextAnalyzer:
	''' Анализатор текста '''

	def __init__(self, page):
		self.page = page

		html = TextParser.get_html(self.page.url)
		self.soup = bs(html, 'html.parser')

		test_request = 'About'
		self.occurrence = self.get_occurrence_request(test_request)
		self.occurrence_20 = self.get_first_occurrence_request(test_request)

	def get_occurrence_request(self, request: str) -> bool:
		'''
		Вхождение запроса
		:params
		~request: str - текст запроса
		'''

		all_text = TextParser.get_all_text(self.soup).lower()
		without_punctuation_text = delete_punctuation_symbols(all_text)
		page_text = without_punctuation_text.replace(' ', '')

		request_text = delete_punctuation_symbols(request)\
			.lower().replace(' ', '')

		if request_text in page_text:
			return True

		return False

	def get_first_occurrence_request(self, request: str) -> bool:
		'''
		Вхождение запроса в первые 20% текста
		:params
		~request: str - текст запроса
		'''

		all_text = TextParser.get_all_text(self.soup).lower()
		first_20_percent_text = get_percent_text(text=all_text, percent=20)
		without_punctuation_text = delete_punctuation_symbols(
			first_20_percent_text)
		page_text = without_punctuation_text.replace(' ', '')
		
		request_text = delete_punctuation_symbols(request)\
			.lower().replace(' ', '')

		if request_text in page_text:
			return True

		return False