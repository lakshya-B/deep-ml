def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	rows = len(matrix)
	columns = len(matrix[0])
	for i in range(rows):
		for j in range(columns):
			matrix[i][j] *= scalar
	return matrix