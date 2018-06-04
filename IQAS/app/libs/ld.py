def LD(qs, ql):
    m, n = len(qs) + 1, len(ql) + 1
    ted_matrix = [[0]*n for i in range(m)]
    for i in range(m):
        ted_matrix[i][0] = i
    for j in range(n):
        ted_matrix[0][j] = j
    for i in range(1, m):
        for j in range(1, n):
            if qs[i - 1] == ql[j - 1]:
                cost = 0
            else:
                cost = 1
            ted_matrix[i][j] = min(ted_matrix[i-1][j] + 1, ted_matrix[i-1][j-1] + cost, ted_matrix[i][j-1] + 1)
    return ted_matrix[m - 1][n - 1]

