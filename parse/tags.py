from bs4 import BeautifulSoup
from bs4 import element


def get_captions(soup: BeautifulSoup) -> tuple:
	h_tags = soup.find_all('h1')
	h_tags.extend(soup.find_all('h2'))
	h_tags.extend(soup.find_all('h3'))

	return tuple(h_tags)


def _is_content_img(img: element.Tag) -> bool:
	href = img.attrs.get('href', '')

	if 'logo' in href or 'icon' in href:
		return False

	return True


def get_images(soup: BeautifulSoup) -> tuple:
	all_imgs = soup.find_all('img')
	filtered_imgs = filter(_is_content_img, all_imgs)

	return tuple(filtered_imgs)