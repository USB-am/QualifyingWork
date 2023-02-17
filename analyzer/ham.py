# hierarchy analysis method

from typing import Union


def P(*args) -> Union[float, int]:
	output = args[0]
	for number in args[1:]:
		output *= number

	return output


# Важность критериев
CRITERION_IMPORTANCE = [
	[1,   9,   5,   8,   7,   8,   3,   4,   2  ],
	[1/9, 1,   1/5, 1/3, 3,   7,   2,   1/2, 8  ],
	[1/5, 5,   1,   1/5, 2,   1/6, 7,   6,   6  ],
	[1/8, 3,   5,   1,   3,   1/5, 8,   2,   6  ],
	[1/7, 1/3, 1/2, 1/3, 1,   1/4, 6,   1/3, 4  ],
	[1/8, 1/7, 6,   5,   4,   1,   8,   1/2, 8  ],
	[1/3, 1/2, 1/7, 1/8, 1/6, 1/8, 1,   1/4, 1/2],
	[1/4, 2,   1/6, 1/2, 3,   2,   4,   1,   7  ],
	[1/2, 1/8, 1/6, 1/6, 1/4, 1/8, 2,   1/7, 1  ],
]

# Случайная согласованность
RANDOM_CONSISTENCY_PARAMS = [0, 0, .58, .9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49]


def get_consistency_attribute(criterion_importance: list,
	                          local_vectors: list) -> float:
	'''
	Расчитывает отношение согласованности
	~params:
	: criterion_importance: list - критерии оценки;
	: local_vectors: list - локальные векторы матрицы
	'''
	n = len(criterion_importance[0])
	# Индекс согласованности (ИС)
	I_max = sum([sum(col)*local_vectors[i] \
		for i, col in enumerate(zip(*criterion_importance))])
	consistency_index = (I_max - n) / (n - 1)
	# Случайная согласованность
	random_consistency = RANDOM_CONSISTENCY_PARAMS[n-1]
	# Отношение согласованности
	consistency_attribute = consistency_index / random_consistency

	return consistency_attribute


def get_criterion_vectors(criterion_importance: list) -> float:
	'''
	Расчитывает локальный векторы критериев.
	~params:
	: criterion_importance: list - критерии оценки
	'''
	n = len(criterion_importance[0])
	# Произведения строк важности
	criterion_product = [P(*row) for row in criterion_importance]
	# Корени от произведения строк важности
	number_root = [product**(1/n) for product in criterion_product]
	# Локальные векторы
	local_vectors = [nr/sum(number_root) for nr in number_root]

	return local_vectors


def get_priority(criterion_vectors: list, vectors: list) -> Union[int, float]:
	s = 0
	for cv, v in zip(criterion_vectors, vectors):
		s += cv * v

	return s


def get_prioritize(data: list, key: str) -> list:
	prioritize = []

	for d1 in data:
		prioritize.append([])

		for d2 in data:
			try:
				value = d1.attrs[key] / d2.attrs[key]
			except ZeroDivisionError:
				value = 1.0

			prioritize[-1].append(value)

	return prioritize


def hierarchy_analysis_method(data: list, criterion_importance: list):
	criterion_vectors = get_criterion_vectors(criterion_importance)
	consistency_attribute = get_consistency_attribute(
		criterion_importance, criterion_vectors)
	# Проверка согласованности
	cc = consistency_attribute <= .1
	# if not cc:
	# 	raise ValueError('Некорректные весы критериев!!!')

	criterions = []
	for key in data[0].attrs.keys():
		prioritize = get_prioritize(data, key)
		vectors = get_criterion_vectors(prioritize)
		criterions.append(vectors)

	# Матрица для расчета глобальных приоритетов
	m = list(zip(*criterions))

	# Определение глобальных приоритетов
	global_priorities = []
	for row in m:
		temp = 0

		for ind, col in enumerate(row):
			value = col * criterion_vectors[ind]
			temp += value

		global_priorities.append(temp)

	max_priority = max(global_priorities)

	return global_priorities.index(max_priority)