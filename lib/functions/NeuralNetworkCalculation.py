from lib.classes.Matrix import *
from lib.classes.ActivationFunction import *
from lib.functions.MatrixOperations.MatrixOperations import *

def NeuralNetworkCalculation(
    weights: list[Matrix],
    xs: Matrix,
    biases: list[Matrix],
    activationFunction: ActivationFunction = None,
    multiclassActivationFunction: MulticlassActivationFunction = None,
    printEachLayer: bool = False,
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

        layer = MatrixActivation(
            matrix=layer,
            activationFunction=activationFunction,
            multiclassActivationFunction=multiclassActivationFunction,
        )
        
        if printEachLayer:
            print(f"Activation [{i}]:")
            MatrixPrinting(layer)
            print("")

    return layer