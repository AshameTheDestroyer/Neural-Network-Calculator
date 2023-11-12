from lib.classes.MatrixElement import *
from math import e

def Sigmoid(x: MatrixElement) -> MatrixElement:
    return (1 + e ** -x) ** -1