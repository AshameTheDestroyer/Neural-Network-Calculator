from lib.classes.Matrix import *
from lib.classes.MatrixElement import *

def MatrixAddition(
    matrix1: Matrix,
    matrix2: Matrix,
) -> Matrix:
    
    width1, height1 = len(matrix1), len(matrix1[0])
    width2, height2 = len(matrix2), len(matrix2[0])

    if width1 != width2 or height1 != height2:
        raise ValueError("Matrices are not addition conformable.")
    
    matrix3: Matrix = []

    for i in range(width1):
        matrix3.append([])
        for j in range(height1):
            if j == 0: matrix3[i].append(0)
            matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return matrix3