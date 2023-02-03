from req import Request
from parse.tools import get_soup


_BASE_URL = 'https://www.google.com/search'


def get_best_page_url(request: Request) -> str:
	soup = get_soup(_BASE_URL, q=request.text, oq=request.text)

	# link_block = soup.find('div', class_='yuRUbf')
	# link_tag = link_block.find('a')
	first_out_block = soup.find('div', class_='yuRUbf')

	if first_out_block is None:
		raise ValueError(f'Невозможно обработать запрос "{request.text}"!')

	first_a_tag = first_out_block.find('a')
	url = first_a_tag.attrs.get('href')

	return url