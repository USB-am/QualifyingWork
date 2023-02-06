from functools import lru_cache


def 


def lev(word_1: str, word_2: str) -> int:
	@lru_cache(None)
	def min_dist(s1: str, s2: str) -> int:
		if s1 == len(word_1) or s2 == len(word_2):
			return len(word_1) - s1 + len(word_2) - s2

		if word_1[s1] == word_2[s2]:
			return min_dist(s1+1, s2+1)

		return 1 + min(
			# insert
			min_dist(s1, s2+1),
			# delete
			min_dist(s1+1, s2),
			# replace
			min_dist(s1+1, s2+1),
		)

	return min_dist(0, 0)


if __name__ == '__main__':
	print(lev('привет', 'привет'))
	print(lev('привет', 'превет'))
	print(lev('привет', 'Превед'))