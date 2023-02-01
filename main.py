# -*- coding: utf-8 -*-

# from parser import Page
import parse


web_resource_url = 'https://habr.com/ru/post/206264/'
#web_resource_url = input(
#	'Enter the url of the web resource you want to analyze: '
#)


def main():
	page = parse.Page(web_resource_url)


if __name__ == '__main__':
	main()