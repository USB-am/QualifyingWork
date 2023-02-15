# -*- coding: utf-8 -*-

from parse import Page
from parse.google_api import get_top_pages
from analyzer import Analyzer
from req import Request


web_resource_url = 'https://habr.com/ru/post/206264/'
# web_resource_url = input(
# 	'Enter the url of the web resource you want to analyze: '
# )

request_text = 'Учим'
# request_text = input(
# 	'Enter the query for which the analysis will be performed:'
# )


def main():
	req = Request(request_text)
	# page = Page(web_resource_url)
	# analyzer = Analyzer(page, req)
	
	pages = get_top_pages(req.text)
	analyzers = [Analyzer(page, req) for page in pages]
	for analyzer in analyzers:
		print(analyzer)
		for attribute, value in analyzer.attrs.items():
			print(f'{attribute} = {value}')
		print()


if __name__ == '__main__':
	main()