from fuzzywuzzy import fuzz, process


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