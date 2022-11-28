from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup as bs


@dataclass
class ImgTag():
	''' <img> '''
	name='img'
	alt: str
	title: str


def get_html(url: str) -> str:
	return requests.get(url).text


def get_images(soup: bs) -> list:
	img_tags = soup.find_all('img')

	imgs = []
	for img in img_tags:
		alt = img.attrs.get('alt')
		title = img.attrs.get('title')
		imgs.append(ImgTag(alt=alt, title=title))

	return imgs


def pars_imgs(url: str) -> list:
	soup = bs(get_html(url), 'html.parser')

	return get_images(soup)