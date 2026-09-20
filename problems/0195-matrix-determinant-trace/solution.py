def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	def determinent(matrix):
		m = len(matrix)
		if m == 1:
			return matrix[0][0]
		if m == 2:
			return matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]

		det = 0
		for col in range(n):
			minor = [row[:col]+row[col+1:] for row in matrix[1:]]
			det += (-1) ** col * matrix[0][col] * determinent(minor)
		return det
	n = len(matrix)
	trace = 0
	for i in range(n):
		trace += matrix[i][i]
	det = determinent(matrix)
	return (det, trace)