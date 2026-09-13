def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here
    min_value = min(x)
    denominator = max(x) - min_value
    result = []
    for value in x:
        result.append((value - min_value)/denominator)
    return result
