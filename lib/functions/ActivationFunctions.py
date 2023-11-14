from enum import Enum
from lib.classes.ActivationFunction import *
from math import tanh, e

class ActivationFunctions(Enum):
    Linear: ActivationFunction = lambda x: x

    HyperbolicTangent: ActivationFunction = lambda x: tanh(x)

    RectifiedLinearUnit: ActivationFunction = lambda x: max(0, x)

    LogisticSigmoid: ActivationFunction = lambda x: (1 + e ** -x) ** -1

    Sign: ActivationFunction = lambda x: -1 if (x < 0) else 1 if (x > 0) else 0

    Heaviside: ActivationFunction = lambda x: 0 if (x < 0) else 1 if (x > 0) else 0.5

    PieceWiseLinear: ActivationFunction = lambda x: 0 if (x <= -0.5) else 1 if (x >= 0.5) else x + 0.5

    def Softmax(xs: list[MatrixElement]) -> list[MatrixElement]:
        summation = sum([e ** x for x in xs])
        return [e ** xi / summation for xi in xs]
