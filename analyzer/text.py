from typing import Union

from parse import Page
from parse.google_api import get_top_page
from req import Request
from .levenshtein import lev


def _mean(*values: Union[int, float]) -> int:
	' Возвращает среднее значение переданных аргументов '

	try:
		output = int(abs(sum(values)) / len(values))
	except ZeroDivisionError:
		output = 0

	return output


def _get_text_percent(text: str, percent: Union[int, float]=100) -> str:
	' Обрезает текст до определенного процента '

	text_length = len(text)
	finish_index = int(text_length / 100 * percent)
	sliced_text = text[:finish_index]

	return sliced_text


class Correlation:
	''' Функционал для сравнения строк '''

	@staticmethod
	def text_text(text_1: str, text_2: str) -> int:
		' Процент сравнения строк '

		if None in (text_1, text_2):
			return 0

		return lev(text_1.lower(), text_2.lower())

	@staticmethod
	def text_list(text: str, words: list) -> int:
		' Процент вхождения слова в список '

		lower_words = tuple(map(lambda s: s.lower(), words))
		output = [lev(text.lower(), word) for word in words]
		value = sum(output)

		return value if value >= 0 else 0


def text_in_text(text_1: str, text_2: str) -> bool:
	'''
	Возвращает True, если text_1 входит в text_2. Иначе - False.
	~params:
	: text_1: str - текст, который должен входить в text_2
	: text_2: str - общий текст в котором ищется вхождение
	'''

	return text_1.lower() in text_2.lower()


def request_in_captions(text: str, captions: Union[list, tuple]) -> int:
	'''
	Возвращает среднее вхождение запроса в теги.
	~params:
	: text: str - запрос;
	: captions: [list, tuple] - список/кортеж тегов.
	'''

	correlation_percents = [Correlation.text_text(text, caption.text) \
		for caption in captions]
	text_inclusion = _mean(*correlation_percents)

	return text_inclusion


def words_in_text(words: list, text: str) -> int:
	'''
	Возвращает количество ключевых слов в тексте
	~params:
	: words: list - список ключевых слов;
	: text: str - текст на странице.
	'''

	counts = sum([text.lower().count(word.lower()) for word in words])

	return counts


def compare_keywords_count(page: Page, request: Request) -> int:
	top_page = get_top_page(request.text)

	other_keywords_count = words_in_text(request.words, top_page.text)
	this_keywords_count = words_in_text(request.words, page.text)

	keywords_percent = (this_keywords_count // other_keywords_count) * 100

	return keywords_percent