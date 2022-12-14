from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup as bs
from bs4 import element
from fuzzywuzzy import fuzz

from analyzer import links_analyze


def get_html(url: str) -> str:
	return requests.get(url).text


class Page():
	''' Базовое представление страницы сайта '''

	def __init__(self, url: str):
		self.url = url
		self.domain = f'{urlparse(url).scheme}://{urlparse(url).netloc}'

		self.__soup = None

	@property
	def soup(self) -> bs:
		if self.__soup is None:
			self.__soup = bs(get_html(self.url), 'html.parser')

		return self.__soup

	def __str__(self):
		return self.domain

	def getElementByTag(self, tag_name: str) -> element.ResultSet:
		return self.soup.find_all(tag_name)

	def getElementByClass(self, class_: str) -> element.ResultSet:
		return self.soup.find_all(False, class_=class_)


URL = 'https://habr.com/ru/post/240463/'
headers = {
	'Content-Type': 'text/html; charset=utf-8',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 '
		'(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
	'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
}


# === Analyzer === #
def title_to_h1(title_text: str, h1_text: str) -> int:
	return fuzz.partial_ratio(title_text, h1_text)
# === Analyzer === #


if __name__ == '__main__':
	page = Page(URL)

	# h1 = page.getElementByTag('h1')[0]
	# title = page.getElementByTag('title')[0]
	# print(title_to_h1(title.text, h1.text))

	links_analyze.links_analyzer(page.domain, page.getElementByTag('a'))