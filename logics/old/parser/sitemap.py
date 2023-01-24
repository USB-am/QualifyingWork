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


def delete_duplicate(func):
	def wrapper(*args, **kwargs):
		links = func(*args, **kwargs)

		return list(set(links))
	return wrapper


def only_this_domain(func):
	def wrapper(page: Page):
		links = func(page)
		page_url = f'{page.scheme}://{page.netloc}'
		output = []

		for link in links:
			parsed_link = urlparse(link)
			temp_link = f'{parsed_link.scheme}://{parsed_link.netloc}'

			if temp_link == page_url:
				output.append(link)

		return output
	return wrapper


def abs_path_to_static(func):
	def wrapper(page: Page):
		links = func(page)

		for ind, link in enumerate(links):
			try:
				if link[0] == '/':
					links[ind] = f'{page.scheme}://{page.netloc}{link}'
			except IndexError:
				continue

		return links
	return wrapper


def delete_empty_links(func):
	def wrapper(*args, **kwargs):
		links = func(*args, **kwargs)

		for link in links:
			if not len(link) or link == '/':
				links.remove(link)

		return links
	return wrapper


def delete_params(func):
	def wrapper(*args, **kwargs):
		links = func(*args, **kwargs)

		for ind, link in enumerate(links):
			links[ind] = link.split('?')[0]

		return links
	return wrapper


def delete_internal_postfix(func):
	def wrapper(*args, **kwargs):
		links = func(*args, **kwargs)

		for ind, link in enumerate(links):
			links[ind] = link.split('#')[0]

		return links
	return wrapper


def tags_to_hrefs(func):
	def wrapper(page: Page):
		link_list = []
		link_tags = func(page)

		for link_tag in link_tags:
			href = link_tag.attrs.get('href')
			if href is None:
				continue

			if not len(href):
				continue

			link_list.append(href)

		return link_list
	return wrapper


@delete_duplicate
@only_this_domain
@abs_path_to_static
@delete_empty_links
@delete_internal_postfix
@delete_params
@tags_to_hrefs
def pars_links(page: Page) -> list:
	html = get_html(page.url)
	soup = bs(html, 'html.parser')

	link_tags = soup.find_all('a')

	return link_tags


class Link:
	links = []

	def __new__(cls, link: str):
		f = list(filter(lambda l: l.link==link, cls.links))
		if f:
			return f[0]

		instance = super(Link, cls).__new__(cls)
		cls.links.append(instance)
		return instance

	def __init__(self, link: str):
		self.link = link
		self.path = urlparse(link).path.split('/')[1:]

	def __str__(self):
		return self.link


class Node:
	''' Представление ветки дерева '''
	nodes = []

	def __new__(cls, parent, link: Link):
		f = list(filter(lambda node: node.link==link, cls.nodes))

		if f:
			return f[0]

		instance = super(Node, cls).__new__(cls)
		cls.nodes.append(instance)
		return instance

	def __init__(self, parent, link: Link):
		self.parent = parent
		self.link = link
		self.childs = []

	def add(self, child) -> None:
		self.childs.append(child)

	def __str__(self):
		return f'{self.link} [{len(self.childs)}]'


def link_path_list_to_dict(links_path: list) -> dict:
	root = Node(None, '')
	for link in links_path:
		current_node = Node(root, link.path[0])

		for app in link.path[1:]:
			new_node = Node(current_node, app)
			current_node.add(new_node)

		root.add(current_node)

	return root


class SiteMap:
	def __init__(self, site: Site):
		self.site = site

	def get_sitemap(self) -> dict:
		link_list = pars_links(Page(self.site.urlroot))
		links = [Link(link) for link in link_list]

		map_ = link_path_list_to_dict(links)

		return map_


if __name__ == '__main__':
	# url = 'https://github.com/USB-am?tab=repositories'
	url = 'https://github.com'
	# url = 'https://azniirkh.vniro.ru/'
	# l1 = Link(url)
	# l2 = Link(url)

	s = Site(url)
	sm = SiteMap(s)

	map_ = sm.get_sitemap()
	# for child in map_.childs:
	# 	print(child)
	print(map_)