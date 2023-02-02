from .tools import get_soup
from . import text as TextParser


def get_page_information(url: str) -> dict:
	'''
	Собирает информацию о веб-странице.
	~params:
	: url: str - url-адрес страницы.
	'''
	soup = get_soup(url)

	output = {
		'title': soup.title.string,
		'h1': soup.h1.string,
		'text': TextParser.get_full_text(soup),
		'description': TextParser.get_meta_content(soup, 'description'),
		'keywords': TextParser.get_keywords(soup),
	}

	return output


class Page:
	' Представление информации о веб-страницы '

	def __init__(self, url: str):
		self.url = url

		page_information = get_page_information(self.url)
		self.__dict__.update(page_information)