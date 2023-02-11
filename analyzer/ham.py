# hierarchy analysis method
from typing import Union


class Node:
	def __init__(self, name: str, value: float, parent=None):
		self.name = name
		self.value = value
		self.parent = parent

	def __str__(self):
		return f'<Node {self.name}>'


class Indicator:
	def __init__(self, name: str, value: Union[int, float]):
		self.name = name
		self.value = value


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
		self._indicators.append(block)
		self._update_titles()

	def _update_titles(self) -> None:
		self.titles = list({titles.add(indicator.name) \
			for indicator in self._indicators})

	def get_importance(self) -> list:
		pass


def main():
	n1 = Node('root', 50)
	n2 = Node('child_1', 45, n1)
	print(n1, n2, sep='\n')


if __name__ == '__main__':
	main()