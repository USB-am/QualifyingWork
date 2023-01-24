import requests
from bs4 import BeautifulSoup as bs


def get_html(url: str) -> str:
	html = requests.get(url).text

	return html


class Meta:
	''' Представление парсера meta тегов '''

	def __init__(self, url: str):
		self.url = url

		self.soup = bs(get_html(self.url), 'html.parser')

		self.description = self.__pars_description()
		self.keywords = self.__pars_keywords()
		self.keywords = ['text_' + str(i).rjust(5, '0') for i in range(1, 16)]

	def __pars_keywords(self) -> list:
		'''
		parse keywords from the meta tag
		:params
		'''

		meta_keywords = self.soup.find('meta', attrs={'name': 'keywords'})
		if meta_keywords is None:
			return []

		content = meta_keywords.attrs.get('content', '')

		# "keyword_1, keyword_2, ..." -> ["keyword_1", "keyword_2", ...]
		keywords = list(map(lambda keyword: keyword.strip(), content.split(',')))

		return keywords

	def __pars_description(self) -> str:
		'''
		parse description from the meta tag
		:params
		'''

		meta_description = self.soup.find('meta', attrs={'name': 'description'})
		if meta_description is None:
			return ''

		content = meta_description.attrs.get('content', '')

		return content