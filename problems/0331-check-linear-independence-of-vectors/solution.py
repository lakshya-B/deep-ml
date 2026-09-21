import numpy as np

def is_linearly_independent(vectors: list[list[float]]) -> bool:
    """
    Check if a set of vectors is linearly independent.
    
    Args:
        vectors: List of vectors, where each vector is a list of floats.
                 All vectors must have the same dimension.
        
    Returns:
        True if vectors are linearly independent, False otherwise.
    """
    # linearly dependend => rank < m'
    vector_list = [row[:] for row in vectors]
    if not vector_list:
        return True
    rows = len(vector_list)
    cols = len(vector_list[0])

    rank = 0
    for c in range(cols):
        pivot_row = None
        for r in range(rank, rows):
            if vector_list[r][c] != 0:
                pivot_row = r
                break
        if pivot_row == None:
            continue
        vector_list[pivot_row], vector_list[rank] = vector_list[rank], vector_list[pivot_row]
        for r in range(rank + 1, rows):
            factor = vector_list[r][c] / vector_list[rank][c]
            for j in range(c,cols):
                vector_list[r][j] -= factor * vector_list[rank][j]
        rank += 1
        if rank == rows:
            break
    return rank == rows
        