import requests
from bs4 import BeautifulSoup as bs
from bs4.element import ResultSet
from bs4.element import Comment
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

	def get_all_text(self) -> tuple:
		html = get_html(self.url).text
		soup = bs(html, 'html.parser')

		def is_visible_tag(tag) -> bool:
			unvisible_tags = ('style', 'script', 'head', 'title',
				'meta', '[document]')
			if tag.parent.name in unvisible_tags:
				return False
			if isinstance(tag, Comment):
				return False
			return True

		texts = soup.find_all(text=True)
		visible_texts = filter(is_visible_tag, texts)

		return tuple(visible_texts)
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
		paragraphs = self.get_all_text()
		density = []

		for paragraph in paragraphs:
			density.append(len(paragraph.text))

		out = (sum(density) / len(density))
		print('({s} / {l}) = {o}'.format(
			s=sum(density),
			l=len(density),
			o=out
		))

		return out

	def get_all_text(self) -> tuple:
		filtered_text = filter(
			lambda tag: not tag.text.strip() in ('', ' ', '\n'),
			self.page.get_all_text()
		)

		return tuple(filtered_text)
# === Analyzer === #
# ================ #


if __name__ == '__main__':
	url = 'https://habr.com/ru/post/206264/'
	# url = 'https://azniirkh.vniro.ru/'

	web_page = WebPage(url)
	analyzer = HeadAnalyzer(web_page)
	# alts = analyzer.images_alts()
	# density = analyzer.text_density()
	# all_text = analyzer.get_all_text()