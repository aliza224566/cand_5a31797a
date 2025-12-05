def standardize_columns(X) -> list[list[float]]:
    if not X:
        return []
    rows, cols = len(X), len(X[0])
    result = [[0]*cols for _ in range(rows)]
    
    for j in range(cols):
        col = [X[i][j] for i in range(rows)]
        mean = sum(col) / rows
        var = sum((x - mean)**2 for x in col) / rows
        std = math.sqrt(var)
        for i in range(rows):
            result[i][j] = round((X[i][j] - mean) / std if std != 0 else 0, 4)
    return result

