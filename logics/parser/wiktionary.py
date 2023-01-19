import requests
from bs4 import BeautifulSoup as bs
from bs4 import element


URL = 'https://ru.wiktionary.org/wiki/{word}'


def get_html(url: str) -> str:
	response = requests.get(url)

	if response.ok:
		return response.text

	raise ValueError(f'Url "{url}" uncorrected!')


# def get_synonyms_block(soup: bs) -> element.Tag:
# 	'''
# 	synonyms_title = soup.find('span', attrs={
# 		'id': "Синонимы", 'class': 'mw-headline'
# 	})
# 	parent_block = synonyms_title.parent
# 	synonyms_block = parent_block.next_sibling
# 	print(dir(parent_block))
# 	print(synonyms_block)
# 	'''
# 	a_tags = soup.find_all('a', title=True)
# 	filtered_tags = filter(lambda a: a.text == a.attrs['title'], a_tags)
# 	# [print(a.text) for a in filtered_tags]


def get_synonyms(word: str) -> list:
	url = URL.format(word=word)
	html = get_html(url)
	soup = bs(html, 'html.parser')

	if not ('синоним' in html.lower()):
		return []

	synonyms_block = get_synonyms_block(soup)
	a_tags = soup.find_all('a', title=True)
	filtered_tags = filter(lambda a: a.text == a.attrs['title'], a_tags)
	synonyms = list(map(lambda tag: tag.text, filtered_tags))

	return synonyms