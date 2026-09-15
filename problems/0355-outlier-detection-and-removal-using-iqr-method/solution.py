import numpy as np

def detect_outliers_iqr(data: list[float], k: float = 1.5) -> dict:
    """
    Detect and remove outliers using the IQR method.

    Args:
        data: List of numerical values
        k: IQR multiplier for determining outlier bounds.

    Returns:
        Dictionary with:
        - cleaned_data
        - outlier_indices
        - lower_bound
        - upper_bound
    """

    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)

    iqr = q3 - q1

    lower_bound = q1 - k * iqr
    upper_bound = q3 + k * iqr

    cleaned_data = []
    outlier_indices = []

    for index, value in enumerate(data):
        if value < lower_bound or value > upper_bound:
            outlier_indices.append(index)
        else:
            cleaned_data.append(round(value, 4))

    return {
        "cleaned_data": cleaned_data,
        "outlier_indices": outlier_indices,
        "lower_bound": round(lower_bound, 4),
        "upper_bound": round(upper_bound, 4)
    }