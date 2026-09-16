import numpy as np

def smote(X_minority: np.ndarray, n_synthetic: int, k: int = 5) -> np.ndarray:
    """
    Generate synthetic samples using SMOTE algorithm.

    Note: the random seed is set by the grader before your function runs,
    so you do NOT need to set it. Just use numpy's global RNG directly
    (np.random.randint, np.random.random, ...).

    Args:
        X_minority: 2D array of minority class samples (n_samples, n_features)
        n_synthetic: Number of synthetic samples to generate
        k: Number of nearest neighbors to consider

    Returns:
        2D array of synthetic samples (n_synthetic, n_features)
    """
    output = []
    # select a base sample
    n_samples = len(X_minority)
    k_actual = min(k, n_samples-1)
    n_features = X_minority.shape[1]
    if k_actual == 0 or n_synthetic == 0:
        return np.empty((0, n_features))
    for _ in range(n_synthetic):
        i = np.random.randint(0, n_samples)
        x_i = X_minority[i]
        # find neighbors
        neighbors = []
        for index in range(n_samples):
            if index == i:
                continue
            point = X_minority[index]
            distance = np.linalg.norm(point - x_i)
            neighbors.append((distance, point))
        neighbors.sort(key=lambda x: x[0])
        nearest_neighbors = neighbors[:k_actual]
        j = np.random.randint(0, k_actual)
        x_nn = nearest_neighbors[j][1]
        gap = np.random.random()
        x_synthetic = x_i + gap*(x_nn - x_i)
        output.append(x_synthetic)

    return np.array(output)
