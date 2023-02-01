import requests
from bs4 import BeautifulSoup


def get_html(url: str, **params) -> str:
	'''
	Возвращает html код страницы
	~params:
	: url: str	- url-адрес страницы;
	: params	- параметры строки запроса
	'''
	html = requests.get(url, **params).text

	return html


def get_soup(html: str) -> BeautifulSoup:
	soup = BeautifulSoup(html, 'hmtl.parser')

	return soup