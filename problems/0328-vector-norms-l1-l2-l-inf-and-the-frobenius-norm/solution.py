import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    arr_shape = arr.shape
    arr_length = len(arr_shape)
    if arr_length == 1:
        range_length = arr_shape[0]
        if norm_type == 'frobenius':
            raise ValueError("can't accept 1D array")
        elif norm_type == 'l1':
            result = 0
            for index in range(range_length):
                result += abs(arr[index])
            return float(result)
        elif norm_type == 'l2':
            result = 0
            for index in range(range_length):
                result += arr[index] ** 2
            return float(np.sqrt(result))
        elif norm_type == 'linf':
            maxi = -np.inf
            for index in range(range_length):
                maxi = max(maxi, abs(arr[index]))
            return float(maxi)
        else:
            raise ValueError("Norm_type Not allowed")
    elif arr_length == 2:
        index1 = arr_shape[0]
        index2 = arr_shape[1]
        if norm_type == 'frobenius' or norm_type == 'l2':
            result = 0
            for i in range(index1):
                for j in range(index2):
                    result += arr[i][j] ** 2
            return float(np.sqrt(result))
        elif norm_type == 'l1':
            result = 0
            for i in range(index1):
                for j in range(index2):
                    result += abs(arr[i][j])
            return float(result)
        elif norm_type == 'linf':
            maxi = -np.inf
            for i in range(index1):
                for j in range(index2):
                    maxi = max(maxi, abs(arr[i][j]))
            return float(maxi)
        else:
            raise ValueError("Norm_type Not allowed")
    else:
        raise ValueError("Only 1D and 2D arrays are allowed")
