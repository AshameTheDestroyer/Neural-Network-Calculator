from tkinter import *

from gui.lib.InputField import *
from gui.Frames.TitledFrame import *

from main import neuralNetwork

def BiasFrame(master: Misc) -> None:
    subFrame = TitledFrame(
        master=master,
        title="Biases",
    )

    def onInputFieldChange(mode: TextChangeMode, value: str) -> None:
        if mode != TextChangeMode.onWrite: return

        neuralNetwork.uniBias = float(value)

    bInputField = InputField(
        master=subFrame,
        minimum=-1000,
        maximum=1000,
        title="Uni-Bias",
        type=InputFieldType.Float,
        text=str(neuralNetwork.uniBias),
        onChange=onInputFieldChange,
    )
    bInputField.pack()