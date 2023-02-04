from parse import Page


def has_tags(page: Page, *tag_names) -> bool:
	'''
	Проверка наличия на странице конкретных тегов.
	~params:
	: page: Page - экземпляр класса Page;
	: tag_names - название тегов.
	'''

	return any([hasattr(page, tag_name) for tag_name in tag_names])


def imgs_number_in_text(text: str, imgs: tuple) -> bool:
	'''
	Проверяет распределение количества картинок на длину текста.
	Оптимально - 1 картинка на каждые 1500 символов текста.
	~params:
	: text: str - текст страницы;
	: imgs: tuple - картинки на странице.
	'''

	text_length = len(text)
	imgs_number = len(imgs)

	return text_length / imgs_number <= 1500