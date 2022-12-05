from dataclasses import dataclass

from bs4 import BeautifulSoup as bs


@dataclass
class ImgTag():
	''' <img> '''
	name='img'
	alt: str
	title: str


def pars_imgs(soup: bs) -> list:
	img_tags = soup.find_all('img')

	imgs = []
	for img in img_tags:
		alt = img.attrs.get('alt')
		title = img.attrs.get('title')
		imgs.append(ImgTag(alt=alt, title=title))

	return imgs