from dataclasses import dataclass
from typing import Union
import re

import requests
from bs4 import BeautifulSoup as bs
from bs4.element import ResultSet


def get_html(url: str) -> str:
	return requests.get(url).text


@dataclass
class TextTag():
	''' Тег с текстом '''
	name: str
	content: str


def select_tags(soup: bs, tag_name: str) -> list:
	p_tags = soup.find_all(tag_name)
	output = []

	for tag in p_tags:
		text = re.sub(r'\s+', ' ', tag.text).strip()
		output.append(TextTag(name=tag_name, content=text))

	return output


def pars_text(soup: bs) -> list:
	output = []

	for tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']:
		output.extend(select_tags(soup, tag_name))

	return output




@dataclass
class LinkTag():
	''' Тег-ссылка '''
	name = 'a'
	content: str
	href: str

	@property
	def catalogs(self) -> list:
		return self.href.split('/')


def pars_links(soup: bs) -> list:
	a_tags = soup.find_all('a')
	output = []

	for tag in a_tags:
		text = re.sub(r'\s+', ' ', tag.text).strip()
		href = tag.attrs.get('href')
		output.append(LinkTag(content=text, href=href))

	return output


@dataclass
class Text():
	texts: Union[list, tuple]

	def __str__(self):
		return self.text

	@property
	def text(self) -> str:
		return '\n'.join(self.texts)

	@property
	def length(self) -> int:
		return len(self.text)

	def first_text_percent(self, limit: int) -> str:
		limit %= 100	# Max percent = 100%
		index_from_percent = self.length // limit
		sliced_text = self.text[:index_from_percent]

		return sliced_text


def pars_all_text(soup: bs) -> str:
	text_tags = pars_text(soup)
	p_tags = map(
		lambda tag: tag.content,
		filter(
			lambda tag: tag.name == 'p',
			text_tags
		)
	)

	return p_tags


def main():
	import requests
	from bs4 import BeautifulSoup as bs

	url = 'https://habr.com/ru/post/704440/'
	html = requests.get(url).text
	soup = bs(html, 'html.parser')
	all_texts = pars_all_text(soup)
	text = Text(texts=tuple(all_texts))

	print(text.first_text_percent(20))


if __name__ == '__main__':
	main()