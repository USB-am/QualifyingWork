# -*- coding: utf-8 -*-

from parse import Page
from analyzer import Analyzer
from req import Request
from parse.google_api import get_top_page


web_resource_url = 'https://habr.com/ru/post/206264/'
# web_resource_url = 'https://amdm.ru/akkordi/fpg/162180/plemya/'
#web_resource_url = input(
#	'Enter the url of the web resource you want to analyze: '
#)


def main():
	req = Request('Изобретаем jpeg')
	print(req)
	# page = Page(web_resource_url)
	# print(page)
	# analyzer = Analyzer(page, req)
	# print(analyzer)
	# print(get_top_page_url(req.text, web_resource_url))
	print(get_top_page(req.text))


if __name__ == '__main__':
	main()