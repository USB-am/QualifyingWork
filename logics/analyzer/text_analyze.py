import requests
from bs4 import BeautifulSoup as bs
from bs4 import element

from . import Page


BLACK_LIST_PARENTS = ('style', 'script', 'head', 'title', 'meta', '[document]')


def get_html(url: str) -> str:
	return requests.get(url).html


def is_visible(tag: element.Tag) -> bool:
	if tag.parent.name in BLACK_LIST_PARENTS:
		return False
	if isinstance(tag, element.Comment):
		return False

	return True


@classmethod
def get_all_text(cls) -> str:
	texts = cls.soup.find_all(text=True)
	visible_text = filter(is_visible, texts)

	return ' '.join(t.strip() for t in visible_text)


class TextAnalyzer:
	''' Анализатор текста '''

	def __init__(self, page: Page):
		self.page = page
		self.soup = bs(get_html(self.page.url), 'html.parser')

		# self.all_text = get_all_text(self.soup)
		self.all_text = get_all_text()