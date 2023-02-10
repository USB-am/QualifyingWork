# hierarchy analysis method

class Node:
	def __init__(self, name: str, value: float, parent=None):
		self.name = name
		self.value = value
		self.parent = parent

	def __str__(self):
		return f'<Node {self.name}>'


def main():
	n1 = Node('root', 50)
	n2 = Node('child_1', 45, n1)
	print(n1, n2, sep='\n')


if __name__ == '__main__':
	main()