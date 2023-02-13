# hierarchy analysis method

from typing import Union


def P(*args) -> Union[float, int]:
	output = args[0]
	for number in args[1:]:
		output *= number

	return output


# Информация
DATA = [
	[1000, 500,  1000, 1, 0, 2000],
	[1800, 200,  500,  2, 1, 1000],
	[800,  1000, 1500, 0, 2, 3000],
	[2000, 500,  100,  0, 0, 500 ],
]

# Важность критериев
CRITERION_IMPORTANCE = [
	[1,   9,   5,   7,   4,   3  ],
	[1/9, 1,   1/5, 1/3, 1/6, 1/7],
	[1/5, 5,   1,   3,   1/2, 1/3],
	[1/7, 3,   1/3, 1,   1/4, 1/5],
	[1/4, 6,   2,   4,   1,   1/2],
	[1/3, 7,   3,   5,   2,   1  ],
]
# Цена товара
CRITERION_PRICE = [
	[1,   7,   1/2, 8  ],
	[1/7, 1,   1/8, 2  ],
	[2,   8,   1,   9  ],
	[1/8, 1/2, 1/9, 1  ],
]
CRITERION_VOLUME = [
	[1,   4,   1/6, 1  ],
	[1/4, 1,   1/6, 1/4],
	[6,   9,   1,   6  ],
	[1,   4,   1/6, 1  ],
]
CRITERION_LOCATION = [
	[1,   1/5, 3, 1/7],
	[5,   1,   7, 1/3],
	[1/3, 1/7, 1, 1/9],
	[7,   3,   9, 1  ],
]
CRITERION_FAILURE = [
	[1,   5,   1/5, 1/5],
	[1/5, 1,   1/9, 1/9],
	[5,   9,   1,   1  ],
	[5,   9,   1,   1  ],
]
CRITERION_TIMES = [
	[1,   5,   7,   1  ],
	[1/5, 1,   3,   1/5],
	[1/7, 1/3, 1,   1/7],
	[1,   5,   7,   1  ],
]
CRITERION_TRANSPORTATION = [
	[1,   1/5, 3, 1/7],
	[5,   1,   7, 1/3],
	[1/3, 1/7, 1, 1/9],
	[7,   3,   9, 1  ],
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


def hierarchy_analysis_method():
	criterion_vectors = get_criterion_vectors(CRITERION_IMPORTANCE)
	consistency_attribute = get_consistency_attribute(
		CRITERION_IMPORTANCE, criterion_vectors)
	# Проверка согласованности
	cc = consistency_attribute <= .1
	if not cc:
		raise ValueError('Некорректные важности критериев!!!')

	price_vectors = get_criterion_vectors(CRITERION_PRICE)
	volume_vectors = get_criterion_vectors(CRITERION_VOLUME)
	location_vectors = get_criterion_vectors(CRITERION_LOCATION)
	failure_vectors = get_criterion_vectors(CRITERION_FAILURE)
	times_vectors = get_criterion_vectors(CRITERION_TIMES)
	transportation_vectors = get_criterion_vectors(CRITERION_TRANSPORTATION)

	price_priority = sum([cv*v for cv, v in zip(criterion_vectors, price_vectors)])
	volume_priority = sum([cv*v for cv, v in zip(criterion_vectors, volume_vectors)])
	location_priority = sum([cv*v for cv, v in zip(criterion_vectors, location_vectors)])
	failure_priority = sum([cv*v for cv, v in zip(criterion_vectors, failure_vectors)])
	times_priority = sum([cv*v for cv, v in zip(criterion_vectors, times_vectors)])
	transportation_priority = sum([cv*v for cv, v in zip(criterion_vectors, transportation_vectors)])

	max_priority = max(price_priority, volume_priority, location_priority,
		failure_priority, times_priority, transportation_priority)

	# print(max_priority)
	return max_priority


if __name__ == '__main__':
	print(hierarchy_analysis_method())