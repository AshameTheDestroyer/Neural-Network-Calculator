from lib.functions.NeuralNetworkCalculation import *
from lib.functions.Sigmoid import *
from lib.classes.MatrixElement import *
from lib.classes.Matrix import *
from math import pi

phi = 0.5 + 5 ** 0.5 * 0.5

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
    [7.24],
    [8.43],
    [-16.67],
    [-12.44],
]

biases: list[Matrix] = [[[0] for j in i] for i in weights]

print("xs:")
MatrixPrinting(xs)
print("")

output = NeuralNetworkCalculation(
    weights=weights,
    xs=xs,
    biases=biases,
    activationFunction=Sigmoid,
    printEachLayer=True,
)