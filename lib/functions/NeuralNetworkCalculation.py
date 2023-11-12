from lib.functions.MatrixOperations.MatrixOperations import *
from lib.classes.Matrix import *

def NeuralNetworkCalculation(
    weights: list[Matrix],
    xs: Matrix,
    biases: list[Matrix],
    activationFunction: Callable[[MatrixElement], MatrixElement],
    printEachLayer: bool = False
) -> Matrix:
    layer = [x for x in xs]

    for weight in weights:
        i = weights.index(weight)

        layer = MatrixMultiplication(weights[i], layer)
        if printEachLayer:
            print(f"Multiplication [{i}]:")
            MatrixPrinting(layer)
            print("")

        layer = MatrixAddition(layer, biases[i])
        if printEachLayer:
            print(f"Addition [{i}]:")
            MatrixPrinting(layer)
            print("")

        layer = MatrixActivation(layer, activationFunction)
        if printEachLayer:
            print(f"Activation [{i}]:")
            MatrixPrinting(layer)
            print("")


    return layer