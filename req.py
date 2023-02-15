import strings


def _get_keywords(text: str) -> tuple:
	'''
	Возвращает список слов из запроса, при этом удаляя знаки пунктуации
	~params:
	: text: str - текст запроса
	'''
	without_punctuation = text.translate(
		str.maketrans('', '', string.punctuation)
	)
	keywords = without_punctuation.split()

	return keywords


class Request:
	'''
	Представление запроса, по которому будет проходить анализ
	~params:
	: text: str - текст запроса
	'''

	def __init__(self, text: str):
		self.text = text
		self.words = _get_keywords(self.text)

	def __str__(self):
		return f'<Request "{self.text}">'