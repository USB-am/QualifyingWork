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


class Link:
	name = 'a'

	def __init__(self, tag: element.Tag):
		self.tag = tag
		self.href = self.__get_href()
		self.text = self.tag.text.strip()

	def __get_href(self) -> str:
		href = self.tag.attrs.get('href')

		if href is None:
			return ''

		if href[0] == '/':
			href = f'https://{DOMAIN}{href}'

		href = href.split('?')[0].split('#')[0]

		return href

	def __str__(self):
		return f'[{self.href}] {self.text}'


class Parser:
	''' Get info from web-page '''

	@staticmethod
	def get_html(url: str) -> str:
		return requests.get(url, headers=headers).text

	def getElementByTag(self, soup: bs, tag: str, **attrs) -> element.ResultSet:
		return soup.find_all(tag, attrs=attrs)

	def get_links(self, url: str) -> list:
		links = []
		html = Parser.get_html(url)
		soup = bs(html, 'html.parser')

		link_tags = self.getElementByTag(soup, 'a')
		for link_tag in link_tags:
			links.append(Link(link_tag))

		return links


class SiteMap(dict):
	''' Inited site map '''

	def __init__(self, domain: str):
		super().__init__()

		self.domain = domain
		self[domain] = []

		self.pars = Parser()
		self.__fill()

	def __fill(self) -> None:
		self.links = self.pars.get_links(self.domain)

		return

	def has_app(self, app_name: str) -> bool:
		return True


class URL:
	def __init__(self, url: str):
		self.url = url.split(DOMAIN)[1]
		self.apps = self.url.split('/')[1:-1]

	def __str__(self):
		return self.url


class Node:
	''' Элемент дерева '''

	def __init__(self, app_name: str, childrens: list=[]):
		self.app_name = app_name
		self.childrens = childrens

	def __in__(self, other: str) -> bool:
		return True
		# TODO: сделать поиск по дочерним элементам


class Tree(dict):
	''' Предсталение дерева приложений сайта '''

	def __init__(self, parent: Node):
		super().__init__()

		self[DOMAIN] = parent

	def add(self, url: URL) -> None:
		current_node = self[DOMAIN]

		for app in url.apps:
			for node in current_node.childrens:
				if app == node.app_name:
					print(f'{app} is exists')
				else:
					print(f'{app} is not found')


if __name__ == '__main__':
	site_map = SiteMap(f'https://{DOMAIN}')

	# for link in site_map.links:
	# 	print(link)
	tree = Tree(Node(app_name=DOMAIN))
	tree.add(URL('https://habr.com/ru/post/683956/'))