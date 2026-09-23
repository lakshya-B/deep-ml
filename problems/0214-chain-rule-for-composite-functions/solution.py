import numpy as np
import math

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""

	def der(function, var):
		if function == 'square':
			return (2 * var, var**2)
		elif function == 'sin':
			return (math.cos(var), math.sin(var))
		elif function == 'exp':
			return (math.exp(var),math.exp(var))
		elif function == 'log':
			return (1/var,math.log(var))

	result = 1
	count = len(functions)
	while count > 0:
		derivative,x = der(functions[count-1],x)
		result *= derivative
		count -=1
	return result

