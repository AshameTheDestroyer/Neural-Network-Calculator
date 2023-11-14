from typing import Callable
from lib.classes.Matrix import *
from lib.classes.ActivationFunction import *
from lib.classes.LayerCalculationStage import *
from lib.functions.MatrixOperations.MatrixOperations import *

def NeuralNetworkCalculation(
    weights: list[Matrix],
    xs: Matrix,
    biases: list[Matrix],
    activationFunction: ActivationFunction = None,
    multiclassActivationFunction: MulticlassActivationFunction = None,
    foreachLayer: Callable[[Matrix, LayerCalculationStage], None] = lambda layer, stage: None,
) -> Matrix:
    layer = [x for x in xs]

    for weight in weights:
        i = weights.index(weight)
        foreachLayer(layer, LayerCalculationStage.onInput)

        layer = MatrixMultiplication(weights[i], layer)
        foreachLayer(layer, LayerCalculationStage.onMultiplication)

        layer = MatrixAddition(layer, biases[i])
        foreachLayer(layer, LayerCalculationStage.onAddition)

        layer = MatrixActivation(
            matrix=layer,
            activationFunction=activationFunction,
            multiclassActivationFunction=multiclassActivationFunction,
        )
        foreachLayer(layer, LayerCalculationStage.onActivation)

    return layer