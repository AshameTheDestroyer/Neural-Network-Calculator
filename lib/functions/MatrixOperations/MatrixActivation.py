from typing import Callable
from lib.classes.MatrixElement import *

def MatrixActivation(matrix: list[list[MatrixElement]], activationFunction: Callable[[MatrixElement], MatrixElement]) -> list[list[MatrixElement]]:
    activatedMatrix: list[list[MatrixElement]] = []
    
    for i in range(len(matrix)):
        activatedMatrix.append([])
        for j in range(len(matrix[i])):
            if j == 0:
                activatedMatrix[i].append(0)
            activatedMatrix[i][j] = activationFunction(matrix[i][j])

    return activatedMatrix