from lib.classes.Matrix import Matrix

def MatrixTranspose(matrix: Matrix) -> Matrix:
    transposedMatrix: Matrix = [[None for i in matrix] for j in matrix[0]]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            try: transposedMatrix[j][i] = matrix[i][j]
            except: transposedMatrix[j][i] = None

    return [list(filter(lambda j: j != None, i)) for i in transposedMatrix]