from urllib.parse import urlparse

from logics.parser import Favicon, Meta


# https://vc.ru/marketing/397043-prodvizhenie-i-raskrutka-veb-sayta-dlya-chego-eto-nuzhno#:~:text=Seo%20продвижение%20веб%20сайта%20способствует,являться%20увеличение%20трафика%20и%20охватов.


class Page:
	''' Базовое представление страницы сайта '''

	def __init__(self, url: str):
		self.url = url
		parsed_url = urlparse(self.url)
		self.netloc = parsed_url.netloc
		self.favicon = Favicon(self.url)
		self.meta = Meta(self.url)

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