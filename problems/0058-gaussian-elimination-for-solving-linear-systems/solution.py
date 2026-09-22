import numpy as np

def gaussian_elimination(A, b):
    """
    Solves the system Ax = b using Gaussian Elimination with partial pivoting.

    :param A: Coefficient matrix
    :param b: Right-hand side vector
    :return: Solution vector x
    """
    A = A.copy()
    b = b.copy()

    n = len(A)

    # Forward elimination
    for c in range(n):
        # Find pivot
        pivot_row = c + np.argmax(np.abs(A[c:, c]))

        # Swap rows
        A[c], A[pivot_row] = A[pivot_row].copy(), A[c].copy()
        b[c], b[pivot_row] = b[pivot_row], b[c]

        # Eliminate below pivot
        for r in range(c + 1, n):
            factor = A[r, c] / A[c, c]

            for j in range(c, n):
                A[r, j] -= factor * A[c, j]

            b[r] -= factor * b[c]

    # Back substitution
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        total = b[i]

        for j in range(i + 1, n):
            total -= A[i, j] * x[j]

        x[i] = total / A[i, i]

    return x