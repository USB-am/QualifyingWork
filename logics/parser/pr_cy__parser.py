# https://a.pr-cy.ru/vk.com/

from logics.parser.parse_tools import get_soup
from logics.tools import Request


__URL = 'https://a.pr-cy.ru/{netloc}/'


def get_metrics(netloc: str) -> dict:
	request = Request(__URL.format(netloc=netloc), {})
	soup = get_soup(request)

	metric_blocks = soup.find_all('div', attrs={'class': 'prcy-hdauij'})
	for metric_block in metric_blocks:
		print(metric_block.text)

	return {}