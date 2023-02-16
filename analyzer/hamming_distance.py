
def hamming_distance(word_1: str, word_2) -> str:
	if (len(word_1) != len(word_2)):
		raise Exception('Strings must be of equal length.')

	dist_counter = 0

	for n in range(len(word_1)):
		if word_1[n] != word_2[n]:
			dist_counter += 1

	return dist_counter


