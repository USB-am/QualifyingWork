from bs4.element import Tag, Comment

from logics.tools import Request


INVISIBLE_TEXT_TAGS = (
	'style',
	'script',
	'head',
	'title',
	'meta',
	'[document]',
)


def is_visible(text_tag: Tag) -> bool:
	if text_tag.parent.name in INVISIBLE_TEXT_TAGS:
		return False
	if isinstance(text_tag, Comment):
		return False

	return True


def get_all_text(request: Request) -> str:
	soup = request.soup
	text_tags = soup.find_all(text=True)
	visible_text_tags = filter(is_visible, text_tags)
	all_text = '\n'.join(t.strip() for t in visible_text_tags)

	return all_text