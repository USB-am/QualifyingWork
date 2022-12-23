# -*- coding: utf-8 -*-

from dataclasses import dataclass
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup as bs
from bs4 import element


URL = 'https://habr.com/ru/post/206264/'
DOMAIN = urlparse(URL).netloc


class Parser():
	@staticmethod
	def get_html(url: str) -> str:
		return requests.get(url).text

	def getElementsByTag(self, html: str, tag: str, attrs: dict={}) -> list:
		soup = bs(html, 'html.parser')

		return soup.find_all(tag, attrs=attrs)

	def getElementsByName(self, html: str, name: str, attrs: dict={}) -> list:
		soup = bs(html, 'html.parser')

		return soup.find_all('', class_=name, attrs=attrs)


@dataclass
class Link():
	''' <a> '''

	def __init__(self, tag: element.Tag):
		self.tag = tag

		self.href = self._find_href()	# tag.attrs.get('href')
		self.text = tag.text.strip()

	def _find_href(self) -> str:
		href = self.tag.attrs.get('href')

		if href is None:
			return ''

		if href[0] == '/':
			href = f'https://{DOMAIN}{href}'

		href = href.split('?')[0].split('#')[0]
		return href

	def __str__(self):
		return f'{self.text} [{self.href}]'


class LinkList(list):
	''' Список ссылок '''

	def __init__(self, link_tags: element.ResultSet):
		self.link_tags = link_tags
		self.__fill_list()

	def __fill_list(self) -> None:
		[self.append(Link(link)) for tag in self.link_tags]


class Page:
	''' Представление страницы сайта '''

	def __init__(self, url: str):
		self.url = url


class Site:
	''' Представление сайта '''

	def __init__(self, domain: str):
		self.domain = domain

		self.parser = Parser()

	def gen_site_map(self) -> dict:
		'''
		Response structure:
			domain: {
				'app_1': {
					'app_1_1': {...}
				},
				'app_2': {
					'app_2_1': {...}
				}
			}
		'''
		html = Parser.get_html(self.domain)
		link_tags = self.parser.getElementsByTag(html, 'a')

		links = []
		for link in link_tags:
			links.append(Link(link))
			print(links[-1])


if __name__ == '__main__':
	site = Site(URL)
	site_map = site.gen_site_map()
	print(site_map)