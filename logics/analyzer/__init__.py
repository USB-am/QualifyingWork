from logics.tools import Request
from logics import parser as Parser
from . import text as TextAnalyzer


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
		self.text = Parser.get_all_text(self.request)

		self.parsed_text = TextAnalyzer.analyze_text(self.text, self.keywords)
		print(f'parsed_text = {self.parsed_text}')

		# self.pr_cy_parser = Parser.PrCyParser(self.request.url.netloc)
		# self.metrics = self.pr_cy_parser.get_metrics()
		# self.visits = self.pr_cy_parser.get_visits()