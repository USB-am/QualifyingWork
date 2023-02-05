from req import Request
from parse.tools import get_soup
from parse import Page


_BASE_URL = 'https://www.google.com/search'
_HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-language': 'ru,en;q=0.9',
}


def get_top_page_url(keywords: str) -> str:
	'''
	Возвращает url лучшего результата в Google поиске.
	~params:
	: keywords: str - текст с запросом
	'''

	soup = get_soup(_BASE_URL, headers=_HEADERS, q=keywords)

	first_block = soup.find('div', class_='yuRUbf')
	a_tag = first_block.find('a')
	href = a_tag.attrs.get('href', '')

	return href


def get_top_page(keywords: str) -> Page:
	page_url = get_top_page_url(keywords)
	page = Page(page_url)

	return page