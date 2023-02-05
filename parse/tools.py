from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


class URL:
	def __init__(self, url: str):
		self.url = url

		parse_url = urlparse(self.url)
		self.netloc = parse_url.netloc
		self.scheme = parse_url.scheme
		self.domain = f'{self.scheme}://{self.netloc}'

	def __str__(self):
		return self.url


def get_html(url: str, headers, **params) -> str:
	'''
	Получает html код страницы
	~params:
	: url: str	- url-адрес страницы;
	: params	- параметры строки запроса.
	'''
	response = requests.get(url, headers=headers, params=params)
	html = response.text

	return html


def get_soup(url: str, headers: dict={}, **params) -> BeautifulSoup:
	'''
	Создает экземпляр класса BeautifulSoup
	~params:
	: url: str	- url-адрес страницы;
	: params	- параметры строки запроса.
	'''
	html = get_html(url, headers, **params)
	soup = BeautifulSoup(html, 'html.parser')

	return soup