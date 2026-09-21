
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	n = len(v)
	num = 0
	den = 0
	for i in range(n):
		num += v[i] * L[i]
		den += L[i] * L[i]
	factor = num/den
	output = []
	for i in range(n):
		output.append(round(factor * L[i] , 3))
	return output
