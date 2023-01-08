from dataclasses import dataclass

from bs4 import element


def delete_internal_links(func):
	def wrapper(*args, **kwargs):
		links = func(*args, **kwargs)
		for link in links:
			link.href = link.href.split('#')[0]

		return links
	return wrapper


def delete_options(func):
	def wrapper(*args, **kwargs):
		links = func(*args, **kwargs)
		for link in links:
			link.href = link.href.split('?')[0]

		return links
	return wrapper


def delete_empty_link(func):
	def wrapper(*args, **kwargs):
		links = func(*args, **kwargs)
		for link in links:
			if len(link.href) == 0:
				links.remove(link)

		return links
	return wrapper


def delete_duplicate(func):
	def wrapper(*args, **kwargs):
		links = func(*args, **kwargs)
		hrefs = []

		for link in links:
			href = link.href
			if href in hrefs:
				links.remove(link)
			else:
				hrefs.append(href)

		return links
	return wrapper


@dataclass
class Link:
	name = 'a'
	text: str
	href: str

	def __str__(self):
		return str(self.href)


@delete_duplicate
@delete_empty_link
@delete_options
@delete_internal_links
def normalize_links(domain: str, links: element.ResultSet) -> list:
	output = []

	for link in links:
		href = link.attrs.get('href')
		if href is None:
			continue

		if href[0] == '/':
			href = domain + href
		text = link.text.strip()

		output.append(Link(text, href))

	return output


class LinksAnalyzer:
	def __init__(self, domain: str, links: element.ResultSet):
		self.domain = domain
		self.links = normalize_links(domain, links)

	def __str__(self):
		return str(self.links)


def links_analyzer(domain: str, links: list) -> None:
	links = normalize_links(domain, links)
	for link in links:
		print(f'{link}')