


class Request:
	'''
	Представление запроса, по которому будет проходить анализ
	~params:
	: text: str - текст запроса
	'''

	def __init__(self, text: str):
		self.text = text

	def __str__(self):
		return f'<Request "{self.text}">'