from functools import lru_cache


def match_percent(func):
	def wrapper(word_1: str, word_2: str, acceptable_percent: int=75):
		changes = func(word_1, word_2)
		word_length = len(word_1)
		percent = 100 - int(changes / word_length * 100)

		if percent >= acceptable_percent:
			return 100

		return percent
	return wrapper


@match_percent
def lev(word_1: str, word_2: str) -> int:
	@lru_cache(None)
	def min_dist(s1: int, s2: int) -> int:
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