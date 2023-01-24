from .analyzer import Analyzer
from .tools import Request


class Page():
	'''
	Базовое представление веб-страницы
	:params
	~request: Request - запрос, включающий URL и headers пользователя
	'''

	def __init__(self, request: Request):
		self.request = request

		self.url = request.url
		self.analyzer = Analyzer(request)

	def __str__(self):
		return f'<Page "{self.url}">'


class Site():
	'''
	Базовое представление веб-ресурса
	:params
	~request: Request - запрос, включающий URL и headers пользователя
	'''

	def __init__(self, request: Request):
		self.request = request

		self.url = request.url
		self.analyzer = Analyzer(request)

	def __str__(self):
		return f'<Site "self.url.domain">'