import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a matrix.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """
    A = A.astype(float).copy()

    m, n = A.shape
    rank = 0

    for col in range(n):

        # Find a pivot row
        pivot_row = None

        for row in range(rank, m):
            if abs(A[row, col]) > tol:
                pivot_row = row
                break

        # No pivot in this column
        if pivot_row is None:
            continue

        # Move pivot row into position
        A[[rank, pivot_row]] = A[[pivot_row, rank]]

        # Eliminate entries below the pivot
        for row in range(rank + 1, m):
            if abs(A[row, col]) > tol:

                factor = A[row, col] / A[rank, col]

                A[row] = A[row] - factor * A[rank]

        rank += 1

        # reached the maximum possible rank
        if rank == m:
            break

    return rank