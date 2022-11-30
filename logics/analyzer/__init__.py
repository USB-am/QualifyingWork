from urllib.parse import urlparse

from ..parsers.head import pars_head
from ..parsers.img import pars_imgs
from ..parsers.text import pars_text, pars_links


def get_domain(url: str) -> str:
	return urlparse(url).netloc


class Analyzer:
	''' Предоставляет методы для анализа сайта '''
	title = 'title'
	metas = ['meta1', 'meta2']

	def __init__(self, url: str):
		self.url = f'https://{url}'
		self.domain = get_domain(self.url)
		self.favicon_url = 'https://github.githubassets.com/favicons/favicon.png'
		self.title, *self.metas = pars_head(self.url)
		self.imgs = pars_imgs(self.url)
		self.text = pars_text(self.url)
		self.links = pars_links(self.url)