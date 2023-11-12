from lib.classes.MatrixElement import *

def MatrixMultiplication(matrix1: list[list[MatrixElement]], matrix2: list[list[MatrixElement]]) -> list[list[MatrixElement]]:
    width1, height1 = len(matrix1), len(matrix1[0])
    width2, height2 = len(matrix2), len(matrix2[0])

    if height1 != width2:
        raise ValueError("Matrices are not multiplication conformable.")
    
    matrix3: list[list[MatrixElement]] = []

    for i in range(width1):
        matrix3.append([])
        for j in range(height2): 
            matrix3[i].append(0)
            for k in range(width2):
                matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return matrix3