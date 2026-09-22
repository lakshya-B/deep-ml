import numpy as np

def calculate_correlation_matrix(X, Y=None):

    def cov(A, B):
        rows, cols_A = A.shape
        _, cols_B = B.shape

        mean_A = []
        mean_B = []

        for j in range(cols_A):
            total = 0

            for i in range(rows):
                total += A[i][j]

            mean_A.append(total / rows)

        for j in range(cols_B):
            total = 0

            for i in range(rows):
                total += B[i][j]

            mean_B.append(total / rows)

        covariance = []

        for i in range(cols_A):
            row = []

            for j in range(cols_B):
                total = 0

                for k in range(rows):
                    total += (
                        (A[k][i] - mean_A[i]) *
                        (B[k][j] - mean_B[j])
                    )

                row.append(total / (rows - 1))

            covariance.append(row)

        return np.array(covariance)

    # If Y is not provided, calculate covariance of X with itself
    if Y is None:
        Y = X

    covariance = cov(X, Y)

    # Variance of each column of X
    var_X = np.diag(cov(X, X))

    # Variance of each column of Y
    var_Y = np.diag(cov(Y, Y))

    std_X = np.sqrt(var_X)
    std_Y = np.sqrt(var_Y)

    correlation = covariance / np.outer(std_X, std_Y)

    return correlation