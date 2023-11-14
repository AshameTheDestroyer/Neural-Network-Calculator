from enum import Enum

class LayerCalculationStage(Enum):
    onInput: str = "input"
    onMultiplication: str = "multiplication"
    onAddition: str = "addition"
    onActivation: str = "activation"