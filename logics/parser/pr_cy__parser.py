# https://a.pr-cy.ru/vk.com/

from bs4 import element

from logics.parser.parse_tools import get_soup
from logics.tools import Request


__URL = 'https://a.pr-cy.ru/{netloc}/'


def get_metrics(netloc: str) -> dict:
	request = Request(__URL.format(netloc=netloc), {})
	soup = get_soup(request)

	metric_blocks = soup.find_all('div', attrs={'class': 'basetest__wrapper'})
	# for metric_block in metric_blocks:
	# 	print(metric_block.text)

	return list(metric_blocks)


def get_visits(netloc: str) -> dict:
	def none_block(block: element.Tag) -> str:
		if block is None:
			return '???'

		return block.text

	request = Request(__URL.format(netloc=netloc), {})
	soup = get_soup(request)

	output = {}

	visitors_block = soup.find('div', class_='prcy-6ze85i e1a2a9ru1')
	# visitors_block = soup.find('div', class_='prcy-6ze85i e1a2a9ru1')
	output['visitors'] = none_block(visitors_block)

	views_block = soup.find('div', class_='prcy-6ze85i e1a2a9ru1')
	output['views'] = none_block(views_block)

	world_place_block = soup.find('div', class_='prcy-19wq853 e1ob7yey6')
	output['world_place'] = none_block(world_place_block)

	county_place_block = soup.find('div', class_='prcy-31uaxh e1ob7yey5')
	output['county_place'] = none_block(county_place_block)

	return output