from bs4 import BeautifulSoup
from bs4.element import Tag, Comment


INVISIBLE_TEXT_TAGS = (
	'style',
	'script',
	'head',
	'title',
	'meta',
	'[document]',
)


def is_visible(text_tag: Tag) -> bool:
	'''
	Возвращает 0, если тег с текстом является невидимым пользователю,
	возвращает 1, если тег с текстом видим для пользователя.
	~params:
	: text_tag: Tag	- объект-тег
	'''
	if text_tag.parent.name in INVISIBLE_TEXT_TAGS:
		return False
	if isinstance(text_tag, Comment):
		return False

	return True


def get_full_text(soup: BeautifulSoup) -> str:
	' Собирает весь видимый текст со страницы '
	text_tags = soup.find_all(text=True)
	visible_text_tags = filter(is_visible, text_tags)
	full_text = '\n'.join(t.strip() for t in visible_text_tags)

	return full_text


def get_meta_content(soup: BeautifulSoup, name: str) -> str:
	meta_tag = soup.find('meta', attrs={'name': name})

	if meta_tag is None:
		return ''

	return meta_tag.attrs.get('content', '')


def get_keywords(soup: BeautifulSoup) -> list:
	keywords = get_meta_content(soup, 'keywords')

	splited_keywords = keywords.split(',')
	keywords_list = list(map(lambda s: s.strip(), splited_keywords))

	return keywords_list