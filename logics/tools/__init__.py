from urllib.parse import urlparse

from django.http.request import HttpHeaders


class URL:
	'''
	Информация о ссылке на веб-страницу
	:params
	~url: str
	'''

	def __init__(self, url: str):
		self.url = url

		url_parse = urlparse(url)
		self.scheme = url_parse.scheme
		self.netloc = url_parse.netloc
		self.path = url_parse.path
		self.domain = f'{self.scheme}://{self.netloc}'

	def __str__(self):
		return self.url


class Request:
	'''
	Представление запроса с дополнительной информацией
	:params
	~url: URL - ссылка на веб-страницу
	~headers: dict - заголовки пользователя
	'''

	def __init__(self, url: URL, headers: HttpHeaders):
		self.url = url
		self.headers = dict(headers)

	def __str__(self):
		return f'<Request {self.url}>'