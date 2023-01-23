import string
from typing import Union
from dataclasses import dataclass
from itertools import product

import requests
from bs4 import BeautifulSoup as bs
from bs4 import element

from logics.parser import text as TextParser
from logics.parser import wiktionary as WikiDict
from logics.parser import google_api as GoogleApi


def delete_punctuation_symbols(text: str) -> str:
	maketrans_text = str.maketrans('', '', string.punctuation)
	translated_text = text.translate(maketrans_text)

	return translated_text


def get_synonyms_from_string(text: str) -> list:
	t = delete_punctuation_symbols(text).lower()
	words = t.split(' ')
	synonyms = []
	for word in key_words:
		synonyms_list = WikiDict.get_synonyms(word)
		if synonyms_list is not None:
			synonyms.extend(synonyms_list)

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


def split_text(text: str) -> list:
	t = delete_punctuation_symbols(text).lower()
	splited_text = t.split(' ')

	return splited_text


def get_inner_synonyms_count(combinations: list, text: str) -> int:
	output = 0
	for combination in combinations:
		combo = ''.join(combination)
		if combo in text:
			output += 1

	return output


@dataclass
class Request:
	'''
	Класс с исформацией о запросе
	'''
	request: str
	clean: int
	partian: int

	def __str__(self):
		return f'<Request ({id(self)})>\nrequest: {self.request}\n' + \
			f'clean: {self.clean}\npartian: {self.partian}\n'

	@property
	def queries(self) -> int:
		return self.clean + self.partian


def get_synonyms_by_key_words(key_words: list) -> list:
	synonyms = []

	for key_word in key_words:
		synonyms_list = WikiDict.get_synonyms(key_word)
		if synonyms_list is not None:
			synonyms.extend(synonyms_list)

	return synonyms


def get_request_entry(request: str, text: str) -> Request:
	clean_entry = text.count(request)
	key_words = split_text(request)

	synonyms = get_synonyms_by_key_words(key_words)
	all_combinations = product(synonyms, repeat=len(key_words))
	partial_entry = get_inner_synonyms_count(all_combinations, text)

	req = Request(request, clean_entry, partial_entry)

	return req


class TextAnalyzer:
	''' Анализатор текста '''

	def __init__(self, page):
		self.page = page

		html = TextParser.get_html(self.page.url)
		self.soup = bs(html, 'html.parser')

		test_request = ' Fire department'
		self.occurrence = self.get_occurrence_request(test_request)
		self.occurrence_20 = self.get_first_occurrence_request(test_request)
		self.distribution = self.even_distribution(test_request)
		self.this_dist, self.other_dist = self.even_distribution(test_request)

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

		without_punctuation_request = delete_punctuation_symbols(request).lower()

		page_text = get_text_for_analyze(self.soup)
		this_mean = get_request_entry(without_punctuation_request, page_text)
		top_1_page = GoogleApi.get_top_page_url(without_punctuation_request)
		top_1_text = get_text_for_analyze(bs(top_1_page, 'html.parser'))
		top_1_mean = get_request_entry(without_punctuation_request, top_1_text)

		try:
			coeff = this_mean.queries / top_1_mean.queries
		except ZeroDivisionError as exc:
			coeff = 1

		print(f'Coeff = {coeff}')

		return this_mean, top_1_mean