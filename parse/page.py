from .tools import get_soup


def get_page_information(url: str) -> dict:
	'''
	Собирает информацию о веб-странице.
	~params:
	: url: str - url-адрес страницы.
	'''
	output = {}

	soup = get_soup(url)
	# print(dir(soup))
	print(soup.title.string)
	print(soup.h1.string)

	return output


class Page:
	''' Представление веб-страницы '''

	def __init__(self, url: str):
		self.url = url

		page_information = get_page_information(self.url)
		self.__dict__.update(page_information)