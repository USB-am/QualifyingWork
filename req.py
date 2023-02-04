def _get_keywords(text: str) -> tuple:
	without_punctuation = text	# DELETE PUNCTUATION SYMBOLS!!!
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