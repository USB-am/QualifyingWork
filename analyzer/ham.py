# hierarchy analysis method
from typing import Union


class Node:
	def __init__(self, name: str, value: float, parent=None):
		self.name = name
		self.value = value
		self.parent = parent

	def __str__(self):
		return f'<Node {self.name}>'


class Indicator(dict):
	def __init__(self, name: str, **kwargs):
		self.name = name
		super().__init__(**kwargs)


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
	i1 = Indicator(name='Indicator 1', title_h1=80, description_req=75)
	i2 = Indicator(name='Indicator 2', title_h1=60, description_req=95)
	i3 = Indicator(name='Indicator 3', title_h1=75, description_req=50)
	i4 = Indicator(name='Indicator 4', title_h1=95, description_req=40)

	M = Matrix()
	M.add_indicator(i1)
	M.add_indicator(i2)
	M.add_indicator(i3)
	M.add_indicator(i4)

	for row in M.get_importance():
		for col in row:
			print(round(col, 2), end=' ')

		print()


if __name__ == '__main__':
	main()