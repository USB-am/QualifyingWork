import requests
from bs4 import BeautifulSoup as bs
from bs4 import element


BLACK_LIST_PARENTS = ('style', 'script', 'head', 'title', 'meta', '[document]')


def get_html(url: str) -> str:
	response = requests.get(url)

	if response.ok:
		return response.text

	raise ValueError(f'Url "{url}" incorrect!')


def is_visible(tag: element.Tag) -> bool:
	if tag.parent.name in BLACK_LIST_PARENTS:
		return False
	if isinstance(tag, element.Comment):
		return False

	return True


def get_all_text(soup: bs) -> str:
	texts = soup.find_all(text=True)
	visible_text = filter(is_visible, texts)

	return ' '.join(t.strip() for t in visible_text)