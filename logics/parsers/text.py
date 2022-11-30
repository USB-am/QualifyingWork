from dataclasses import dataclass
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


def select_text_tags(soup: bs) -> list:
	output = []

	for tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']:
		output.extend(select_tags(soup, tag_name))

	return output


def pars_text(url: str):
	soup = bs(get_html(url), 'html.parser')

	return select_text_tags(soup)




@dataclass
class LinkTag():
	''' Тег-ссылка '''
	name = 'a'
	content: str
	href: str

	@property
	def catalogs(self) -> list:
		return self.href.split('/')


def select_a_tags(soup: bs) -> list:
	a_tags = soup.find_all('a')
	output = []

	for tag in a_tags:
		text = re.sub(r'\s+', ' ', tag.text).strip()
		href = tag.attrs.get('href')
		output.append(LinkTag(content=text, href=href))

	return output


def pars_links(url: str) -> list:
	soup = bs(get_html(url), 'html.parser')

	return select_a_tags(soup)