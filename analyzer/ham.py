# hierarchy analysis method
from typing import Union


class Indicator(dict):
	def __init__(self, name: str, **kwargs):
		self.name = name
		super().__init__(**kwargs)


def build_matrix(ind_1: Indicator, ind_2: Indicator) -> list:
	titles = tuple(ind_1.keys())
	m = []

	for row in range(len(titles)):
		m.append([])
		for col in range(len(titles)):
			if col == row:
				value = 1
			elif col > row:
				value = ind_1.get(titles[col], 0) / ind_2.get(titles[col], 0)
			elif col < row:
				value = ind_2.get(titles[col], 0) / ind_1.get(titles[col], 0)
			m[-1].append(value)

	return m


def get_max_indicator(indicators: list) -> Indicator:
	def get_max(ind_1: Indicator, ind_2: Indicator) -> Indicator:
		matrix = []
		for title in ind_1.keys():
			pass

	max_indicator = get_max(indicators[0], indicators[1])

	for indicator in indicators[2:]:
		max_indicator = get_max(max_indicator, indicator)

	return max_indicator


class Matrix:
	def __init__(self):
		self._indicators = []
		self.titles = []

	def add_indicator(self, indicator: Indicator) -> None:
		'''
		Добавляет новый показатель
		~params:
		: indicator: Indicator - экземпляр класса Indicator
		'''
		self._indicators.append(indicator)
		self._update_titles()

	def _update_titles(self) -> None:
		titles = set()

		for indicator in self._indicators:
			for key in indicator.keys():
				titles.add(key)

		self.titles = titles

	def get_importance(self) -> list:
		matrix = []
		
		for ind in self._indicators:
			for title in self.titles:
				matrix.append([])

				for i in self._indicators:
					value = ind.get(title, 0) / i.get(title, 1)
					matrix[-1].append(value)

		return matrix


def main():
	args_1 = {
		'price': 1000,
		'volume': 500,
		'marker': 1000,
		'errors': 1,
		'moving': 2000,
	}
	args_2 = {
		'price': 1800,
		'volume': 200,
		'marker': 500,
		'errors': 2,
		'moving': 1000
	}
	i1 = Indicator(name='Indicator 1', **args_1)
	i2 = Indicator(name='Indicator 2', **args_2)
	i3 = Indicator(name='Indicator 3', title_h1=75, description_req=50)
	i4 = Indicator(name='Indicator 4', title_h1=95, description_req=40)

	M = Matrix()
	M.add_indicator(i1)
	M.add_indicator(i2)
	M.add_indicator(i3)
	M.add_indicator(i4)

	# for row in M.get_importance():
	# 	for col in row:
	# 		print(round(col, 2), end=' ')

	# 	print()

	for row in build_matrix(i1, i2):
		for col in row:
			print(round(col, 2), end=' ')

		print()


if __name__ == '__main__':
	main()