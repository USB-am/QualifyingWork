from req import Request
from parse.tools import get_soup


_BASE_URL = 'https://www.google.com/search'


def get_top_page_url(key_request: str) -> str:
	'''
	Получает лучший (первый) результат в выдаче поисковика
	по принимаемому запросу и возвращает url этой страницы
	:params
	~key_request: str - ключевое слово/запрос
	'''

	soup = get_soup(_BASE_URL, q=key_request.text)

	first_a_tag = soup.find('div', class_='yuRUbf').find('a')
	url = URL(first_a_tag.attrs.get('href', ''))

	return url