from typing import Union

from fuzzywuzzy import fuzz, process


def _mean(*values: int) -> int:
	return int(sum(values) / len(values))


def _get_text_percent(text: str, percent: Union[int, float]=100) -> str:
	' Обрезает текст до определенного процента '

	text_length = len(text)
	finish_index = int(text_length / 100 * percent)
	sliced_text = text[:finish_index]

	return sliced_text


class Correlation:
	''' Функционал для сравнения строк '''
	# https://habr.com/ru/post/491448/

	@staticmethod
	def text_text(text_1: str, text_2: str) -> int:
		' Процент сравнения строк '

		return fuzz.WRatio(text_1, text_2)

	@staticmethod
	def text_list(text: str, words: list) -> int:
		' Процент вхождения слова в список '

		return process.extractOne(text, words)


def text_in_text(text_1: str, text_2: str) -> bool:
	'''
	Возвращает True, если text_1 входит в text_2. Иначе - False.
	~params:
	: text_1: str - текст, который должен входить в text_2
	: text_2: str - общий текст в котором ищется вхождение
	'''

	return text_1 in text_2


def request_in_captions(text: str, captions: Union[list, tuple]) -> int:
	correlation_percents = [Correlation.text_text(text, caption.text) \
		for caption in captions]
	text_inclusion = _mean(*correlation_percents)

	return text_inclusion