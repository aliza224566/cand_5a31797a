import math

def standardize_columns(X):
    if not X:
        return []

    rows = len(X)
    cols = len(X[0])

    out = [[0]*cols for _ in range(rows)]

    for j in range(cols):
        col = [X[i][j] for i in range(rows)]
        mean = sum(col) / rows
        var = sum((v - mean) ** 2 for v in col) / rows
        std = math.sqrt(var)

        if std == 0:
            for i in range(rows):
                out[i][j] = 0.0
        else:
            for i in range(rows):
                out[i][j] = round((X[i][j] - mean) / std, 4)

    return out
