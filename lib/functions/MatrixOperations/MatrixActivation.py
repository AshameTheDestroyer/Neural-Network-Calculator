from lib.classes.Matrix import *
from lib.classes.MatrixElement import *
from lib.classes.ActivationFunction import *
from .MatrixTranspose import *

def MatrixActivation(
    matrix: Matrix,
    activationFunction: ActivationFunction,
    layeredActivationFunction: LayeredActivationFunction,
) -> Matrix:
    if activationFunction is not None:
        return [[activationFunction(j) for j in i] for i in matrix]
    elif layeredActivationFunction is not None:
        return MatrixTranspose([layeredActivationFunction(i) for i in MatrixTranspose(matrix)])
    else:
        raise ValueError("No activation function was provided.")