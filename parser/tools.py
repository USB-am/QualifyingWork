import requests
from bs4 import BeautifulSoup


def get_html(url: str, **params) -> str:
	'''
	Получает html код страницы
	~params:
	: url: str	- url-адрес страницы;
	: params	- параметры строки запроса.
	'''
	html = requests.get(url, **params).text

	return html


def get_soup(url: str, **params) -> BeautifulSoup:
	'''
	Создает экземпляр класса BeautifulSoup
	~params:
	: url: str	- url-адрес страницы;
	: params	- параметры строки запроса.
	'''
	html = get_html(url, **params)
	soup = BeautifulSoup(html, 'hmtl.parser')

	return soup