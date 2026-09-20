def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	exp_x = 0
	exp_x2 = 0
	for index in range(1,n+1):
		exp_x += (index) * (1/n)
		exp_x2 += ((index) ** 2) * (1/n)
	var = exp_x2 - (exp_x)**2
	return (exp_x, var)



