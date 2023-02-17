# -*- coding: utf-8 -*-

from parse.google_api import get_top_pages
from analyzer import Analyzer
from req import Request
from analyzer.ham import hierarchy_analysis_method as HAM
from analyzer.ham import CRITERION_IMPORTANCE


request_text = 'Изобретаем JPEG'
# request_text = input(
# 	'Enter the query for which the analysis will be performed:'
# )


TRANSLATE_INDICATOR_NAME = {
	'title_to_h1': 'Соотношение текста из тега TITLE с первым текстом из тега H1',
	'title_to_req': 'Соотношение текста из тега TITLE с вводимым пользователем запросом',
	'req_in_text': 'Процент вхождения ключевых слов, из вводимого пользователем запроса, по отношению к основному тексту страницы;',
	'req_words_count': 'Количество ключевых слов в тексте страницы',
	'req_in_20text': 'Наличие вхождения запроса в первые 20% текста страницы',
	'keywords_description': 'Наличие ключевых слов, вводимые пользователем в запросе, в META-теге описания страницы (с атрибутом name равным description)',
	'has_list_or_table': 'Наличие на странице хотя бы одной таблицы или перечисления (table, ol или ul)',
	'req_in_h': 'Вхождение ключевых слов в тегах H1, H2, H3',
	'imgs_number': 'Наличие изображений на каждые 1 500 символов сплошного текста',
}


def main():
	req = Request(request_text)

	pages = get_top_pages(req.text)
	analyzers = [Analyzer(page, req) for page in pages]
	
	priority_web_resource_index = HAM(analyzers, CRITERION_IMPORTANCE)
	priority_web_resource = analyzers[priority_web_resource_index]

	print('Вывод:\nНаиболее релевантным веб-ресурсам среди'
		f'проанализированных является "{priority_web_resource.page.url}".\n\n'
		'В результате проведенного анализа были получены следующие значения:'
	)
	for key, value in priority_web_resource.attrs.items():
		param_name = TRANSLATE_INDICATOR_NAME.get(key, '')
		print(f'\t- {param_name} = {value}')


if __name__ == '__main__':
	main()