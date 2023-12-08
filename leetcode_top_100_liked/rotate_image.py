def rotate(matrix):
    l = 0
    r = len(matrix) - 1

    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    matrix.reverse()


    return matrix


print(rotate([[1,2,3],[4,5,6],[7,8,9]]))