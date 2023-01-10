'''
import sys
import logging
from pysitemap import crawler


exclude_urls = ('.pdf', '.jpg', '.jpeg', '.png', '?', '.zip', '.rar', '.ico')


if __name__ == '__main__':
	if '--iocp' in sys.argv:
		from asyncio import events, windows_events
		sys.argv.remove('--iocp')
		logging.info('using iocp')
		el = windows_events.ProactorEventLoop()
		events.set_event_loop(el)

	# root_url = sys.argv[1]
	root_url = 'https://www.haikson.com'
	c = crawler(root_url, out_file='sitemap.txt', out_format='txt', exclude_urls=exclude_urls)
	print(dir(c), c, type(c))
'''

from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup as bs


def get_html(url: str) -> str:
	return requests.get(url).text


class Site:
	''' Базовое представление сайта '''

	def __init__(self, urlroot: str):
		self.urlroot = urlroot
		self.netloc = urlparse(urlroot).netloc


class Page:
	''' Базовое представление страницы '''

	def __init__(self, url: str):
		self.url = url
		self.scheme = urlparse(url).scheme
		self.netloc = urlparse(url).netloc
		self.path = urlparse(url).path.split('/')[1:]


def delete_internal_postfix(func):
	def wrapper(page: Page):
		links = func(page)

		for link in links:
			href = link.attrs.get('href')
			if href is None:
				link.attrs['href'] = f'{page.scheme}://{page.netloc}'
				continue

			if not len(href):
				continue

			if href[0] == '/':
				link.attrs['href'] = f'{page.scheme}://{page.netloc}{href}'

		return links
	return wrapper


@delete_internal_postfix
def pars_links(page: Page) -> list:
	html = get_html(page.url)
	soup = bs(html, 'html.parser')

	link_tags = soup.find_all('a')

	return link_tags


class Link:
	links = []

	def __new__(cls, link: str):
		f = list(filter(lambda l: l.link==link, cls.links))
		if list(f):
			return list(f)[0]

		instance = super(Link, cls).__new__(cls)
		cls.links.append(instance)
		return instance

	def __init__(self, link: str):
		self.link = link

	def __str__(self):
		return self.link


class SiteMap:
	def __init__(self, site: Site):
		self.site = site

	def get_dict(self) -> dict:
		output = {
			self.site.netloc: pars_links(Page(self.site.urlroot)),
		}

		return output


if __name__ == '__main__':
	url = 'https://github.com/USB-am?tab=repositories'
	url = 'https://github.com'
	l1 = Link(url)
	l2 = Link(url)
	# print(l1)
	# print(l2)

	s = Site(url)
	sm = SiteMap(s)

	print(sm.get_dict())