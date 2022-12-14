import requests
from bs4 import BeautifulSoup as bs
from bs4.element import ResultSet
from fuzzywuzzy import fuzz

# ============== #
# === Parser === #
def get_html(url: str) -> requests.models.Response:
	response = requests.get(url)

	if response.ok:
		return response

	raise requests.exceptions.RequestException(
		f'[{response.status_code}] Fail GET-request!')


class WebPage():
	''' Представление веб-страницы '''

	def __init__(self, url: str):
		self.url = url

	def get_elements_by_tag(self, tag: str, attrs: dict={}) -> ResultSet:
		html = get_html(self.url).text
		soup = bs(html, 'html.parser')

		return soup.find_all(tag, attrs=attrs)
# === Parser === #
# ============== #

# ================ #
# === Analyzer === #
class HeadAnalyzer():
	''' Анализатор <head> '''

	def __init__(self, page: WebPage):
		self.page = page

	def percent_title_to_h1(self) -> int:
		try:
			title_tag = self.page.get_elements_by_tag('title')[0]
			h1_tag = self.page.get_elements_by_tag('h1')[0]

			return fuzz.partial_ratio(title_tag.text, h1_tag.text)
		except IndexError:
			return 0

	def images_alts(self) -> float:
		imgs = self.page.get_elements_by_tag('img')
		imgs_count = 0
		imgs_has_alt = 0

		for img in imgs:
			if not img.attrs.get('alt') in (None, ''):
				imgs_has_alt += 1
			imgs_count += 1

		return imgs_has_alt / imgs_count

	def text_density(self) -> float:
		paragraphs = self.page.get_elements_by_tag('p')
		density = []

		for paragraph in paragraphs:
			density.append(len(paragraph.text))

		return (sum(density) / len(density)) / 500
# === Analyzer === #
# ================ #


if __name__ == '__main__':
	url = 'https://habr.com/ru/post/206264/'
	# url = 'https://azniirkh.vniro.ru/'

	web_page = WebPage(url)
	analyzer = HeadAnalyzer(web_page)
	# alts = analyzer.images_alts()
	# density = analyzer.text_density()