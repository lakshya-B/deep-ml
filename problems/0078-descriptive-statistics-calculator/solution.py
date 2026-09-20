import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    data.sort()
    length = len(data)
    total = 0
    median = 0
    counter = {}
    if length % 2 == 0:
        median = (data[length//2] + data[length//2 - 1]) / 2
    else:
        median = data[length//2]
    for index in range(length):
        ele = data[index]
        total += ele
        if ele in counter:
            counter[ele] += 1
        else:
            counter[ele] = 1
    mode = 0
    maxi = -np.inf
    for key, value in counter.items():
        if value > maxi:
            mode = key
            maxi = value
    mean = total/length
    sq_sum = 0
    for index in range(length):
        sq_sum += (data[index] - mean)**2
    variance = sq_sum/length
    standard_deviation = (variance)**(0.5)
    q1= np.percentile(data, 25)
    q2= np.percentile(data, 50)
    q3= np.percentile(data, 75)
    IQR = q3 - q1

    return {'mean':mean, 'median':median, 'mode': mode, 'variance': variance, 'standard_deviation':standard_deviation,'25th_percentile':q1, '50th_percentile':q2, '75th_percentile':q3, 'interquartile_range':q3-q1}