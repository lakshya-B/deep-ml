def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    if not vectors:
        return []

    n_features = len(vectors)
    n_observations = len(vectors[0])

    # Calculate mean of each feature
    means = []
    for vector in vectors:
        means.append(sum(vector) / n_observations)

    # Calculate covariance matrix
    covariance = []

    for i in range(n_features):
        row = []

        for j in range(n_features):
            total = 0.0

            for k in range(n_observations):
                total += (
                    (vectors[i][k] - means[i])
                    * (vectors[j][k] - means[j])
                )

            cov = total / (n_observations - 1)
            row.append(cov)

        covariance.append(row)

    return covariance