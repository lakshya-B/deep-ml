import numpy as np
from scipy import stats

def impute_missing_data(data: np.ndarray, strategy: str = 'mean') -> np.ndarray:
    """
    Impute missing values in a 2D array using the specified strategy.
    
    Args:
        data: 2D numpy array with missing values represented as np.nan
        strategy: Imputation strategy - 'mean', 'median', or 'mode'
        
    Returns:
        2D numpy array with missing values imputed
    """
    # Your code here
    column0 = []
    column1 = []
    data_length = len(data)
    nan_indices = []
    for i in range(data_length):
        for j in range(2):
            value = data[i][j]
            if np.isnan(value):
                nan_indices.append((i,j))
            elif j % 2 == 0:
                column0.append(value)
            else:
                column1.append(value)
    mean0 = np.mean(column0)
    mean1 = np.mean(column1)
    median0 = np.median(column0)
    median1 = np.median(column1)
    mode0 = stats.mode(column0).mode
    mode1 = stats.mode(column1).mode

    if strategy == 'mean':
        for i,j in nan_indices:
            if j%2 == 0:
                data[i][j] = mean0
            else:
                data[i][j] = mean1
    elif strategy == 'median':
        for i,j in nan_indices:
            if j%2 == 0:
                data[i][j] = median0
            else:
                data[i][j] = median1
    elif strategy == 'mode':
        for i,j in nan_indices:
            if j%2 == 0:
                data[i][j] = mode0
            else:
                data[i][j] = mode1
    else:
        print("strategy must be 'mean', 'median', or 'mode'")
    return data
