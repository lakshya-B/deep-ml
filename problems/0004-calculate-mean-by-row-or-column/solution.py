def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	rows = len(matrix)
	columns = len(matrix[0])
	means = []
	if mode == 'row':
		for i in range(rows):
			summ = 0
			for j in range(columns):
				summ += matrix[i][j]
			means.append(summ/columns) 

	else:
		for j in range(columns):
			summ = 0
			for i in range(rows):
				summ += matrix[i][j]
			means.append(summ/rows)

	return means