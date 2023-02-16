# -*- coding: utf-8 -*-

from parse.google_api import get_top_pages
from analyzer import Analyzer
from req import Request

from analyzer.ham import hierarchy_analysis_method, CRITERION_IMPORTANCE


request_text = 'Изобретаем JPEG'
# request_text = input(
# 	'Enter the query for which the analysis will be performed:'
# )


def main():
	req = Request(request_text)

	pages = get_top_pages(req.text)
	analyzers = [Analyzer(page, req) for page in pages]
	# for analyzer in analyzers:
	# 	print(analyzer)
	# 	for attribute, value in analyzer.attrs.items():
	# 		print(f'{attribute} = {value}')
	# 	print('\n'*3)
	print(f'hierarchy_analysis_method = ', end='')
	print(hierarchy_analysis_method(analyzers, CRITERION_IMPORTANCE))

	# excel = ExcelWriter(f'effectiveness_web_resources_{req.text}.xlsx')
	# excel.write(analyzers)


if __name__ == '__main__':
	main()