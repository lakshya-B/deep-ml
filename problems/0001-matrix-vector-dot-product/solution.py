import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.

	vector_length = len(b)
	rows = len(a)
	columns = len(a[0])
	if vector_length != rows:
		return -1
	result = [0] * columns
	for i in range(rows):
		for j in range(columns):
			result[i] += a[i][j] * b[j]
	return result
			