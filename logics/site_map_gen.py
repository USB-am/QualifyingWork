# -*- coding: utf-8 -*-

from urllib.parse import urlparse
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup as bs
from bs4 import element


_URL = 'https://habr.com/ru/post/240463/'
DOMAIN = urlparse(_URL).netloc
headers = {
	'Content-Type': 'text/html; charset=utf-8',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 '
		'(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
	'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
}


def get_html(url: str) -> str:
	html = requests.get(url).text

	return html


@dataclass
class Page():
	''' Базовое представление страницы сайта '''
	url: str


class SiteTree(dict):
	''' Представление карты сайта '''

	def __init__(self, domain: str, root: Page):
		super().__init__(domain=root)

	def add_node(self, child: Page) -> None:
		print(f'add_node has child={child}')


class Site:
	''' Базовое представление сайта '''

	def __init__(self, url: str):
		self.url = url
		self.domain = urlparse(url).netloc
		self.page = Page(self.domain)

		self.childs = SiteTree(self.domain, self.page)

	def __str__(self):
		return self.domain


def main():
	site = Site(_URL)


if __name__ == '__main__':
	main()