from urllib.parse import urlparse

from logics.parser import Favicon, Meta


class Page:
	''' Базовое представление страницы сайта '''

	def __init__(self, url: str):
		self.url = url

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