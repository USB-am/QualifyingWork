import requests
from bs4 import BeautifulSoup as bs

from logics.tools import Request


def get_html(request: Request, **parameters) -> str:
	html = requests.get(
		request.url,
		#headers=request.headers,
		params=parameters
	).text

	return html


def get_soup(request: Request) -> bs:
	html = get_html(request)
	soup = bs(html, 'html.parser')

	return soup