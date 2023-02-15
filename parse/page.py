from bs4 import BeautifulSoup

from .tools import get_soup
from . import text as TextParser
from . import tags as TagParser


def _get_tag(soup: BeautifulSoup, tag_name: str, text: bool=True) -> str:
	tag = getattr(soup, tag_name)

	if text:
		if tag is not None:
			return tag.string

		return ''

	return tag


def get_page_information(url: str) -> dict:
	'''
	Собирает информацию о веб-странице.
	~params:
	: url: str - url-адрес.
	'''
	soup = get_soup(url)

	output = {
		'title': _get_tag(soup, 'title'),
		'h1': _get_tag(soup, 'h1'),
		'ul': _get_tag(soup, 'ul', False),
		'ol': _get_tag(soup, 'ol', False),
		'table': _get_tag(soup, 'table', False),
		'text': TextParser.get_full_text(soup),
		'description': TextParser.get_meta_content(soup, 'description'),
		'keywords': TextParser.get_keywords(soup),
		'captions': TagParser.get_captions(soup),
		'imgs': TagParser.get_images(soup),
	}

	return output


class Page:
	' Представление информации о веб-страницы '

	def __init__(self, url: str):
		self.url = url

		page_information = get_page_information(self.url)
		self.__dict__.update(page_information)

	def __str__(self):
		return f'<Page "{self.url}">'