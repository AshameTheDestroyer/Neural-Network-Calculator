from typing import Callable
from lib.classes.MatrixElement import *

ActivationFunction = Callable[[MatrixElement], MatrixElement]
LayeredActivationFunction = Callable[[list[MatrixElement]], list[MatrixElement]]