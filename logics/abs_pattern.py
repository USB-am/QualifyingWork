from dataclasses import dataclass
from abc import ABC

import requests
from bs4 import BeautifulSoup as bs
from bs4 import element
from fuzzywuzzy import fuzz


url = 'https://habr.com/ru/post/206264/'


class Container():
	''' Container for Parser, Analyzer and Model '''


class Parser():
	def __init__(self, url: str):
		self.url = url

		html = requests.get(self.url)
		self.soup = bs(html.text, 'html.parser')

	def get_element(self, tag: str, attrs: dict={}) -> element.Tag:
		return self.soup.find(tag, attrs=attrs)

	def get_elements(self, tag: str, attrs: dict={}) -> element.ResultSet:
		return self.soup.find_all(tag, attrs=attrs)


@dataclass
class Analyzer():
	def __call__(self, parser: Parser):
		return {
			'title': self._percent_title_to_h1(parser),
		}

	def _percent_title_to_h1(self, parser: Parser) -> float:
		title_tag = parser.get_element('title')
		h1_tag = parser.get_element('h1')

		return fuzz.partial_ratio(title_tag.text, h1_tag.text)


@dataclass
class Model(ABC):
	''' Абстрактный класс модели '''
	analyzer: Analyzer


class BlogModel(Model):
	''' Математическая модели для оценки сайтов типа "блок" '''


if __name__ == '__main__':
	pars = Parser(url)
	analyzer = Analyzer()

	data = analyzer(pars)
	print(data['title'])