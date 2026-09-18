def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    rows_a = len(a)
    columns_a = len(a[0])
    rows_b = len(b)
    columns_b = len(b[0])
    if columns_a != rows_b:
        return -1
    c = [[0] * columns_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(columns_a):
            for k in range(columns_b):
                c[i][k] += a[i][j]*b[j][k]
    return c