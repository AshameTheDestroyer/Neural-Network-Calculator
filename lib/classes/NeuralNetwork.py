from lib.classes.Event import *
from lib.classes.Matrix import *
from lib.classes.ActivationFunction import *
from lib.classes.ActivationFunctions import *
from lib.functions.NeuralNetworkCalculation import *
from lib.functions.MatrixOperations.MatrixTranspose import *

class NeuralNetwork():
    inputs: Matrix
    biases: list[Matrix]
    weights: list[Matrix]
    outputs: Matrix
    dimensions: list[(int, int)]
    
    activationFunction: ActivationFunction
    multiclassActivationFunction: MulticlassActivationFunction

    onDimensionAltered: Event
    onNetworkCalculated: Event

    def __init__(self) -> None:
        self.inputs = []
        self.biases = []
        self.weights = []
        self.outputs = []
        self.dimensions = []

        self.activationFunction = ActivationFunctions.Linear
        self.multiclassActivationFunction = None

        self.onDimensionAltered = Event()
        self.onNetworkCalculated = Event()

    def addDimensions(self, *lengths: list[int]) -> None:
        for i in range(len(lengths)):
            dimension = self._addDimension(lengths[i], isLastLayer=(i == len(lengths) - 1))
            matrix = NeuralNetwork._buildMatrix(dimension)

            if i == 0:
                self.inputs = matrix
                continue
            
            if i == len(lengths) - 1:
                self.weights[-1] = NeuralNetwork._buildMatrix(self.dimensions[-2])
                self.outputs = matrix
                continue

            self.weights.append(matrix)

    def alterDimension(self, index: int, dimension: tuple[int, int]) -> None:
        (width, height) = dimension
        self._setDimension(index, (width, height))

        if index > 0:
            self._setDimension(index - 1, (self.dimensions[index - 1][0], width))
        
        if index < len(self.dimensions) - 1:
            self._setDimension(index + 1, (height, self.dimensions[index + 1][1]))

    def appendDimension(self, length: int) -> None:
        self.dimensions[-1] = (self.dimensions[-1][0], length)

        weight = NeuralNetwork._buildMatrix(self.dimensions[-1])
        self.weights.append(weight)

        self.dimensions.append((length, 1))
        self._alterMatrix(self.outputs, self.dimensions[-1])

    def popDimension(self) -> None:
        self.dimensions.pop()
        self.weights.pop()
        self.dimensions[-1] = (self.dimensions[-1][0], 1)
        self._alterMatrix(self.outputs, self.dimensions[-1])

    def calculate(self) -> None:
        self.outputs = NeuralNetworkCalculation(
            xs=MatrixTranspose([i for i in self.inputs]),
            weights=[MatrixTranspose(i) for i in self.weights],
            biases=[[[0] for k in j] for j in [MatrixTranspose(i) for i in self.weights]],
            activationFunction=self.activationFunction,
            multiclassActivationFunction=self.multiclassActivationFunction,
        )

        self.onNetworkCalculated.Fire(self.outputs)

    def _addDimension(self, length: int, isLastLayer: bool = False) -> tuple[int, int]:
        if len(self.dimensions) == 0:
            self.dimensions.append((1, length))
        elif isLastLayer:
            self.dimensions[-1] = (self.dimensions[-1][0], length)
            self.dimensions.append((length, 1))
        else:
            self.dimensions.append((self.dimensions[-1][1], length))
        
        return self.dimensions[-1]

    def _setDimension(self, index: int, dimension: tuple[int, int]) -> None:
        self.dimensions[index] = dimension
        matrix: Matrix

        if index == 0: matrix = self.inputs
        elif index == len(self.dimensions) - 1: matrix = self.outputs
        else: matrix = self.weights[index - 1]
        
        self._alterMatrix(matrix, dimension)
        self.onDimensionAltered.Fire(index, dimension, matrix)

    def _alterMatrix(self, matrix: Matrix, dimensions: tuple[int, int]) -> None:
        (newWidth, newHeight) = dimensions
        oldWidth, oldHeight = len(matrix), len(matrix[0])
        
        if newWidth > oldWidth:
            for i in range(newWidth - oldWidth):
                matrix.append([0 for j in range(oldHeight)])
        elif newWidth < oldWidth:
            for i in range(oldWidth - newWidth):
                matrix.pop()

        if newHeight > oldHeight:
            for row in matrix:
                for i in range(newHeight - oldHeight):
                    row.append(0)
            
        elif newHeight < oldHeight:
            for row in matrix:
                for i in range(oldHeight - newHeight):
                    row.pop()
            
    def _buildMatrix(dimensions: tuple[int, int]) -> Matrix:
        (width, height) = dimensions
        return [[0 for j in range(height)] for i in range(width)]
