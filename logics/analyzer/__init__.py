from logics.tools import Request
from logics import parser as Parser


class Analyzer:
	'''
	Базовый класс, хранящий результаты анализа веб-страницы
	:params
	~request: Request - ссылка на веб-страницу
	'''

	def __init__(self, request: Request):
		self.request = request

	@property
	def favicon(self) -> str:
		return Parser.get_favicon(self.request)

	@property
	def description(self) -> str:
		return Parser.get_description(self.request)

	@property
	def keywords(self) -> list:
		return Parser.get_keywords(self.request)

	@property
	def metrics(self) -> dict:
		return Parser.get_metrics(self.request.url.netloc)