import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	indices = len(gradient)
	squares = 0
	for index in range(indices):
		squares += (gradient[index]) ** 2
	magnitude = np.sqrt(squares)
	if magnitude == 0:
		return {'magnitude':magnitude, 'direction':[0]*indices, 'descent_direction':[0]*indices}
	direction = gradient / magnitude
	descent_direction = -1 * direction
	return {'magnitude':magnitude, 'direction':direction, 'descent_direction':descent_direction}