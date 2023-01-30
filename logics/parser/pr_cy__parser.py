# https://a.pr-cy.ru/vk.com/

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


def get_visits(netloc: str) -> str:
	request = Request(__URL.format(netloc=netloc), {})
	soup = get_soup(request)

	visits_block = soup.find('div', class_='prcy-6ze85i e1a2a9ru1')
	print(visits_block.text)