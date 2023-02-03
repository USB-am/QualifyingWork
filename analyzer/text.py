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


def text_in_text(text_1: str, text_2: str) -> bool:
	'''
	Возвращает True, если text_1 входит в text_2. Иначе - False.
	~params:
	: text_1: str - текст, который должен входить в text_2
	: text_2: str - общий текст в котором ищется вхождение
	'''

	return text_1 in text_2