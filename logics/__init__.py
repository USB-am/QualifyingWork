from urllib.parse import urlparse

from logics.parser import Favicon, Meta
from logics.analyzer.text_analyze import TextAnalyzer


class Page:
	''' Базовое представление страницы сайта '''

	def __init__(self, url: str):
		self.url = url
		parsed_url = urlparse(self.url)
		self.netloc = parsed_url.netloc
		self.favicon = Favicon(self.url)
		self.meta = Meta(self.url)
		self.text = TextAnalyzer(self)

	def __str__(self):
		return f'<Page url={self.url}>'


class Site:
	''' Базовое представление сайта '''

	def __init__(self, domain: str):
		self.domain = domain
		self.netloc = urlparse(self.domain).netloc
		self.childs = {
			self.domain: Page(self.domain),
		}
		self.favicon = Favicon(self.domain)
		self.meta = Meta(self.domain)

	def __str__(self):
		return f'<Site domain={self.domain}>'