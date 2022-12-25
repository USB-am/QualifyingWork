# -*- coding: utf-8 -*-

from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup as bs
from bs4 import element


URL = 'https://habr.com/ru/post/240463/'
DOMAIN = urlparse(URL).netloc
headers = {
	'Content-Type': 'text/html; charset=utf-8',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 '
		'(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
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
	'''
	Inited site map. Has structure:
	{
		domain: [
			{
				'app_1': [
					{
						'app_1_1': [...]
					},
					...
				],
				...
			},
			...
		]
	}

	'''

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


if __name__ == '__main__':
	site_map = SiteMap(f'https://{DOMAIN}')

	for link in site_map.links:
		print(link)