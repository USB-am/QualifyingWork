import re

from logics.parser.parse_tools import get_soup
from logics.tools import Request


def get_favicon(request: Request) -> str:
	soup = get_soup(request)

	favicon_tag = soup.find('link', attrs={'rel': re.compile('.*icon.*')})

	if favicon_tag is None:
		return ''

	return favicon_tag.attrs.get('href', '')