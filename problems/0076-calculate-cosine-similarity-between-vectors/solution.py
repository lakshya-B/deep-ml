import numpy as np

def norm(v):
	result = 0
	for index in range(len(v)):
		result += v[index] ** 2
	return np.sqrt(result)

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	arr_length = len(v1)
	dot_product = 0
	for index in range(arr_length):
		dot_product += v1[index] * v2[index]
	return float(dot_product)/(norm(v1) * norm(v2))