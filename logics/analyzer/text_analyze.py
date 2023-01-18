import string
from typing import Union
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup as bs
from bs4 import element

from logics.parser import text as TextParser
from logics.parser import wiktionary as WikiDict


def delete_punctuation_symbols(text: str) -> str:
	maketrans_text = str.maketrans('', '', string.punctuation)
	translated_text = text.translate(maketrans_text)

	return translated_text


def get_synonyms_from_string(text: str) -> list:
	t = delete_punctuation_symbols(text)
	words = t.split(' ')
	synonyms = []
	for word in words:
		s = WikiDict.get_synonyms(word)
		synonyms.extend(s)

	return synonyms


def get_text_for_analyze(soup: bs) -> str:
	all_text = TextParser.get_all_text(soup)
	without_punctuation_text = delete_punctuation_symbols(all_text)
	page_text = without_punctuation_text.replace(' ', '').lower()

	return page_text


def get_percent_text(text: str, percent: Union[float, int]) -> str:
	text_length = len(text)
	index = int(text_length * percent / 100)

	return text[:index]


@dataclass
class Request:
	'''
	Класс с исформацией о запросе
	'''
	request: str
	clean: int
	partian: int

	def __str__(self):
		return f'<Request "{request}">'


def get_request_entry(request: str, text: str) -> Request:
	clean_entry = text.count(request)
	# synonyms = get_synonyms_from_string(request)
	words = delete_punctuation_symbols(request)
	words = t.split(' ')
	synonyms = [*WikiDict.get_synonyms(word) for word in words]
	all_combinations = product(synonyms, repeat=len(words))
	partial_entry = None


class TextAnalyzer:
	''' Анализатор текста '''

	def __init__(self, page):
		self.page = page

		html = TextParser.get_html(self.page.url)
		self.soup = bs(html, 'html.parser')

		test_request = 'About'
		self.occurrence = self.get_occurrence_request(test_request)
		self.occurrence_20 = self.get_first_occurrence_request(test_request)
		self.distribution = self.even_distribution(test_request)

	def get_occurrence_request(self, request: str) -> bool:
		'''
		Вхождение запроса
		:params
		~request: str - текст запроса
		'''

		page_text = get_text_for_analyze(self.soup)

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

		page_text = get_text_for_analyze(self.soup)
		first_20_percent_text = get_percent_text(text=page_text, percent=20)
		
		request_text = delete_punctuation_symbols(request)\
			.lower().replace(' ', '')

		if request_text in first_20_percent_text:
			return True

		return False

	def even_distribution(self, request: str) -> float:
		'''
		Частота запроса в тексте по отношению к ТОП-1 сайту
		в списке выдачи поисковика
		:params
		~request: str - запрос
		'''

		page_text = get_text_for_analyze(self.soup)
		this_mean = get_request_entry(requests, page_text)

		return 'even_distribution'