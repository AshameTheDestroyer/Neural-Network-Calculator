from typing import Callable
from lib.classes.MatrixElement import *

ActivationFunction = Callable[[MatrixElement], MatrixElement]
ConvolutionalActivationFunction = Callable[[list[MatrixElement]], list[MatrixElement]]