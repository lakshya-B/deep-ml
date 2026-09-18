import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    length_g = len(g_coeffs)
    length_h = len(h_coeffs)
    g_x = g_x_1 = h_x = h_x_1 = 0
    for i in range(length_g):
        g_x += g_coeffs[i] * ((x)**(length_g-i-1))
        if (length_g-i-2) < 0:
            break
        g_x_1 += g_coeffs[i] * (length_g-i-1) * ((x)**(length_g-i-2))
    for i in range(length_h):
        h_x += h_coeffs[i] * ((x)**(length_h-i-1))
        if (length_h-i-2) < 0:
            break
        h_x_1 += h_coeffs[i] * (length_h-i-1) * ((x)**(length_h-i-2))
    num_dev = g_x_1 * h_x - g_x * h_x_1
    den_dev = (h_x) ** 2
    return num_dev/den_dev