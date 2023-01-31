from logics.tools import URL, Request
from .text import get_all_text


HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-language': 'ru,en;q=0.9',
}


_BASE_URL = 'https://www.google.com/search'


def get_top_page_url(key_request: str) -> URL:
	'''
	Получает лучший (первый) результат в выдаче поисковика
	по принимаемому запросу и возвращает url этой страницы
	:params
	~key_request: str - ключевое слово/запрос
	'''

	html = get_html(_BASE_URL, q=key_request)
	soup = bs(html, 'html.parser')

	first_a_tag = soup.find('div', class_='yuRUbf').find('a')
	url = URL(first_a_tag.attrs.get('href', ''))

	return url


def get_top_page_text(key_request: str) -> str:
	url = get_top_page_url(key_request)
	request = Request(url, headers=HEADERS)
	text = get_all_text(request)

	return text