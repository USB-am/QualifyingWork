from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup as bs
from bs4.element import ResultSet


@dataclass
class MetaTag():
	''' <meta> '''
	name = 'meta'
	type: str
	content: str


@dataclass
class TitleTag():
	''' <title> '''
	name = 'title'
	text: str


@dataclass
class LinkTag():
	''' <link> '''
	name = 'link'
	rel: str
	href: str


def get_html(url: str) -> str:
	return requests.get(url).text


def select_seo_meta_tags(soup: bs) -> list:
	def get_meta_by_name(name: str) -> str:
		try:
			return soup.find('meta', attrs={'name': name}) \
				.attrs.get('content')
		except AttributeError as error:
			return None

	def get_meta_by_http_equiv(name: str) -> str:
		try:
			return soup.find('meta', attrs={'http-equiv': name}) \
				.attrs.get('content')
		except AttributeError as error:
			return None

	seo_meta_tags = [
		MetaTag(type='description', content=get_meta_by_name('description')),
		MetaTag(type='robots', content=get_meta_by_name('robots')),
		MetaTag(type='googlebot', content=get_meta_by_name('googlebot')),
		MetaTag(type='google', content=get_meta_by_name('google')),
		MetaTag(type='google-site-verification',
		        content=get_meta_by_name('google-site-verification')),
		MetaTag(type='http-equiv', content=get_meta_by_http_equiv('Content-Type')),
		MetaTag(type='viewport', content=get_meta_by_name('viewport')),
		MetaTag(type='rating', content=get_meta_by_name('rating')),
	]

	return seo_meta_tags


def select_favicon_tag(soup: bs) -> LinkTag:
	tag = soup.find('link', attrs={'rel': 'icon'})

	return LinkTag(rel='icon', href=tag.attrs.get('href'))


def pars_head(url: str) -> list:
	soup = bs(get_html(url), 'html.parser')

	return [
		TitleTag(text=soup.find('title').text),
		select_favicon_tag(soup),
		*select_seo_meta_tags(soup),
	]