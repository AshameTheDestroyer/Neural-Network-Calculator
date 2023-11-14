from lib.classes.Matrix import *
from lib.classes.MatrixElement import *
from lib.classes.ActivationFunction import *
from .MatrixTranspose import *

def MatrixActivation(
    matrix: Matrix,
    activationFunction: ActivationFunction,
    multiclassActivationFunction: MulticlassActivationFunction,
) -> Matrix:
    if activationFunction is not None:
        return [[activationFunction(j) for j in i] for i in matrix]
    elif multiclassActivationFunction is not None:
        return MatrixTranspose([multiclassActivationFunction(i) for i in MatrixTranspose(matrix)])
    else:
        raise ValueError("No activation function was provided.")