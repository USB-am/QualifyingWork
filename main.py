# -*- coding: utf-8 -*-

from parse import Page
from analyzer import Analyzer
from req import Request


web_resource_url = 'https://habr.com/ru/post/206264/'
# web_resource_url = input(
# 	'Enter the url of the web resource you want to analyze: '
# )

request_text = 'Изобретаем jpeg'
# request_text = input(
# 	'Enter the query for which the analysis will be performed:'
# )


def main():
	req = Request('Изобретаем jpeg')
	page = Page(web_resource_url)
	analyzer = Analyzer(page, req)
	print(analyzer.attrs)


if __name__ == '__main__':
	main()