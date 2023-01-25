from logics.parser.parse_tools import get_soup
from logics.tools import Request


def get_desctiption(request: Request) -> str:
	soup = get_soup(request)

	meta_tag = soup.find('meta', attrs={'name': 'description'})
	if meta_tag is None:
		return ''

	return meta_tag.attrs.get('content', '')


def get_keywords(request: Request) -> list:
	soup = get_soup(request)

	meta_tag = soup.find('meta', attrs={'name': 'keywords'})
	if meta_tag is None:
		return []

	keywords = meta_tag.attrs.get('content', '')
	splited_keywords = keywords.split(',')
	valid_keywords = list(map(lambda keyword: keyword.strip(), splited_keywords))

	return valid_keywords