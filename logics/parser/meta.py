import requests
from bs4 import BeautifulSoup as bs


def get_html(url: str) -> str:
	html = requests.get(url).text

	return html


class Meta:
	''' Представление парсера meta тегов '''

	def __init__(self, url: str):
		self.url = url
		self.description = self.__pars_description()

	def __pars_description(self) -> str:
		html = get_html(self.url)
		soup = bs(html, 'html.parser')

		meta_description = soup.find('meta', attrs={'name': 'description'})
		if meta_description is None:
			return ''

		content = meta_description.attrs.get('content')
		if content is None:
			return ''

		return content