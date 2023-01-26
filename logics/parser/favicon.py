import re
from dataclasses import dataclass

from bs4.element import ResultSet

from logics.parser.parse_tools import get_soup
from logics.tools import Request


@dataclass
class Favicon:
	'''
	Представление инонки веб-страницы
	:params
	~href: str - путь до иконки
	~size: tuple - размер иконки
	'''

	href: str
	size: tuple

	def __str__(self):
		return f'<Favicon {self.size}>'


def get_maximum_size_icon(favicon_tags: ResultSet) -> Favicon:
	icons = []

	for tag in favicon_tags:
		sizes = tag.attrs.get('sizes', '0x0')
		size = tuple(map(int, sizes.split('x')))

		icon = Favicon(
			href=tag.attrs.get('href'),
			size=size
		)
		icons.append(icon)

	sorted_icons_by_size = sorted(icons, key=lambda icon: sum(icon.size))

	return sorted_icons_by_size[0]


def get_favicon(request: Request) -> str:
	soup = get_soup(request)

	favicon_tags = soup.find_all('link', attrs={'rel': re.compile('.*icon.*')})
	max_size_icon = get_maximum_size_icon(favicon_tags)

	if favicon_tags[0] is None:
		return ''

	return favicon_tags[0].attrs.get('href', '')