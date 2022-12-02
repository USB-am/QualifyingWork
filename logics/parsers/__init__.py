import requests
from bs4 import BeautifulSoup as bs

# from .google_parser import GoogleParser
from .head import pars_title, pars_meta_tags, pars_favicon
from .img import pars_imgs
from .text import pars_text, pars_links


def get_html(url: str) -> str:
	return requests.get(url).text


class WebPage():
	''' Базовый класс web-страницы '''

	def __init__(self, url: str):
		self.url = url

	def get_data(self) -> dict:
		html = get_html(self.url)
		soup = bs(html, 'html.parser')

		data = {
			'title': pars_title(soup),
			'meta_tags': pars_meta_tags(soup),
			'favicon': pars_favicon(soup),
			'imgs': pars_imgs(soup),
			'text': pars_text(soup),
			'links': pars_links(soup),
		}

		return data