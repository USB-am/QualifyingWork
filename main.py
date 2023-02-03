# -*- coding: utf-8 -*-

from parse import Page
from analyzer import Analyzer
from req import Request
from parse.google import get_best_page_url


web_resource_url = 'https://habr.com/ru/post/206264/'
#web_resource_url = input(
#	'Enter the url of the web resource you want to analyze: '
#)


def main():
	req = Request('jpeg')
	print(req)
	page = Page(web_resource_url)
	print(page)
	analyzer = Analyzer(page, req)
	print(analyzer)
	print(get_best_page_url(req))


if __name__ == '__main__':
	main()