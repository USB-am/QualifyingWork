import requests
from bs4 import BeautifulSoup as bs


def get_html(url: str) -> str:
	html = requests.get(url).text

	return html


class Favicon:
	def __init__(self, domain: str):
		self.domain = domain
		self.href = self.__parse_href()

	def __parse_href(self) -> str:
		soup = bs(get_html(self.domain), 'html.parser')
		icon_tag = soup.find('link', attrs={'rel': 'icon'})

		if icon_tag is None:
			return ''

		href = icon_tag.attrs.get('href')
		if href is not None:
			if href[0] == '/':
				href = self.domain + href

		return href