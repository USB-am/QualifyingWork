import requests
from bs4 import BeautifulSoup as bs


HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-language': 'ru,en;q=0.9',
}


BASE_URL = 'https://www.google.com/search'


def get_html(url: str, **parameters) -> str:
	html = requests.get(url, headers=HEADERS, params=parameters).text

	return html


def get_top_page_url(request: str) -> str:
	'''
	Получает лучший (первый) результат в выдаче поисковика
	по принимаемому запросу
	:params
	~request: str - текст (запрос)
	'''

	html = get_html(BASE_URL, q=request)
	soup = bs(html, 'html.parser')

	first_a_tag = soup.find('div', class_='yuRUbf').find('a')
	url = first_a_tag.attrs.get('href', '')

	return url