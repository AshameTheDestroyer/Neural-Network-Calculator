from typing import Callable
from lib.classes.MatrixElement import *

ActivationFunction = Callable[[MatrixElement], MatrixElement]
MulticlassActivationFunction = Callable[[list[MatrixElement]], list[MatrixElement]]