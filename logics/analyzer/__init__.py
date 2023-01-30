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

		self.favicon = Parser.get_favicon(self.request)
		self.description = Parser.get_description(self.request)
		self.keywords = Parser.get_keywords(self.request)

		self.pr_cy_parser = Parser.PrCyParser(self.request.url.netloc)
		self.metrics = self.pr_cy_parser.get_metrics()
		self.visits = self.pr_cy_parser.get_visits()