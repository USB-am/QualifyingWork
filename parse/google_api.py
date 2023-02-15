from req import Request
from parse.tools import get_soup
from parse import Page


_BASE_URL = 'https://www.google.com/search'
_HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-language': 'ru,en;q=0.9',
}


def get_top_page_url(keywords: str) -> list:
	'''
	Возвращает url лучшего результата в Google поиске.
	~params:
	: keywords: str - текст с запросом
	'''

	soup = get_soup(_BASE_URL, headers=_HEADERS, q=keywords)

	first_blocks = soup.find_all('div', class_='yuRUbf')[:5]
	hrefs = [first_block.find('a').attrs.get('href', '') \
		for first_block in first_blocks]

	return hrefs


def get_top_page(keywords: str) -> Page:
	page_url = get_top_page_url(keywords)[0]
	page = Page(page_url)

	return page


def get_top_pages(keywords: str) -> list:
	page_urls = get_top_page_url(keywords)
	pages = [Page(page_url) for page_url in page_urls]

	return pages