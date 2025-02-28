def matrix_multiply(m1, m2):
    m1r = len(m1)
    m1c = len(m1[0])
    n2r = len(m2)
    n2c = len(m2[0])

    if m1c != n2r:
        return -1
    
    result = [[0 for i in range(n2c)] for j in range(m1r)]
    # for each row in m1
    for i in range(m1r): 
        # for each column in m2
        for j in range(n2c): 
            # for each position in result
            for k in range(m1c): 
                result[i][j] += m1[i][k] * m2[k][j]

    return result


m1 = [[2, 3], [1, 4]]
m2 = [
    [5, 7, 9], 
    [6, 8, 10]
]
m3 = [
    [5, 6], 
    [7, 8], 
    [9, 10]
]
print(matrix_multiply(m3, m1))
