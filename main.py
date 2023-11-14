from math import pi
from lib.classes.Matrix import *
from lib.classes.MatrixElement import *
from lib.classes.ActivationFunction import *
from lib.classes.LayerCalculationStage import *
from lib.functions.ActivationFunctions import *
from lib.functions.NeuralNetworkCalculation import *

phi = 0.5 + 5**0.5 * 0.5

weights: list[Matrix] = [
    [
        [5, 1, 1, 2],
        [4, 6, -5, 4],
        [5, 1, 5, 1 / 2],
    ],
    [
        [1, 1, 1],
        [3, 4, -5],
        [5, 1, 1],
        [5 / 2, 4, 2],
    ],
    [
        [2, 6, 1, 2],
        [4, 4, -5, 4],
        [9, 1, 5, 3],
    ],
]

xs: Matrix = [
    [10 * pi],
    [-17.63],
    [2 * phi**0.5],
    [-34.17],
]

biases: list[Matrix] = [[[0] for j in i] for i in weights]

print("xs:")
MatrixPrinting(xs)
print("")


def foreachLayer(layer: Matrix, stage: LayerCalculationStage):
    match stage:
        case (
            LayerCalculationStage.onMultiplication |
            LayerCalculationStage.onActivation |
            LayerCalculationStage.onAddition
        ):
            print(f"{stage.value.title()}:")
            MatrixPrinting(layer)
            print("")
        case _:
            return


output = NeuralNetworkCalculation(
    weights=weights,
    xs=xs,
    biases=biases,
    # activationFunction=ActivationFunctions.Sign,
    multiclassActivationFunction=ActivationFunctions.Softmax,
    foreachLayer=foreachLayer
)
