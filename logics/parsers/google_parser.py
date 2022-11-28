import os
import json

from bs4 import BeautifulSoup as bs
from . import base_parser as parser

from urllib.parse import urlparse


API_KEY = os.environ['GoogleApiKey']


class GoogleParser():
	''' Парсит данные из поискового ответа Google '''
	CX = '006f62468f00e4aa6'
	URL = 'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&cr=false&lr={language}&start={start}&q=link:{domain}'
	LANGUAGE = 'ru'

	def __init__(self, url: str):
		self.url = url
		self.domain = urlparse(self.url).netloc

	def get_pages(self, start: int=0) -> list:
		google_links_url = GoogleParser.URL.format(
			api_key=API_KEY,
			cx=GoogleParser.CX,
			domain=self.domain,
			language=GoogleParser.LANGUAGE,
			start=start,
		)
		pages = json.loads(parser.get_html(google_links_url))

		return pages