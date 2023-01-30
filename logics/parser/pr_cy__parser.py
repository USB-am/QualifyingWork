from bs4 import element

from logics.parser.parse_tools import get_soup
from logics.tools import URL, Request


_URL = 'https://a.pr-cy.ru/{netloc}/'


class PrCyParser:
	'''
	Парсер сайта https://a.pr-cy.ru/
	~params
	:netloc: str - домен сайта
	'''

	def __init__(self, netloc: str):
		self.url = URL(_URL.format(netloc=netloc))
		self.request = Request(self.url, {})

		self.metrics = self.get_metrics()
		self.visits = self.get_visits()

	def get_metrics(self) -> dict:
		metric_blocks = self.request.soup.find_all(
			'div', class_='basetest__wrapper'
		)

		return metric_blocks


	def get_visits(self) -> dict:
		output = {}

		visitors_block = self.request.soup.find(
			'div', class_='prcy-6ze85i e1a2a9ru1'
		)
		output['visitors'] = self.none_block(visitors_block)

		views_block = self.request.soup.find(
			'div', class_='prcy-6ze85i e1a2a9ru1'
		)
		output['views'] = self.none_block(views_block)

		world_place_block = self.request.soup.find(
			'div', class_='prcy-19wq853 e1ob7yey6'
		)
		output['world_place'] = self.none_block(world_place_block)

		county_place_block = self.request.soup.find(
			'div', class_='prcy-31uaxh e1ob7yey5'
		)
		output['county_place'] = self.none_block(county_place_block)

		return output

	def none_block(self, block: element.Tag) -> str:
		if block is None:
			return '???'

		return block.text