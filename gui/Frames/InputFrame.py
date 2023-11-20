from tkinter import *

from gui.lib.InputField import *
from gui.Frames.TitledFrame import *
from lib.functions.MatrixOperations.MatrixTranspose import *

from main import neuralNetwork

def InputFrame(master: Misc) -> None:
    subFrame = TitledFrame(
        master=master,
        title="Input",
    )

    xInputFields: list[InputField] = []

    def onCountInputFieldChange(mode: TextChangeMode, text: str) -> None:
        if mode != TextChangeMode.onWrite: return
        
        count = int(text)
        neuralNetwork.alterDimension(0, (1, count))
        
        if count > len(xInputFields):
            for i in range(len(xInputFields), count):
                def onInputFieldChange(mode: TextChangeMode, value: str, i = i) -> None:
                    if mode != TextChangeMode.onWrite: return

                    neuralNetwork.inputs[0][i] = float(value)

                xInputField = InputField(
                    master=subFrame,
                    title="x" + str(i + 1).zfill(2),
                    type=InputFieldType.Float,
                    minimum=-100,
                    maximum=100,
                    onChange=onInputFieldChange,
                    text=str(neuralNetwork.inputs[0][i]),
                )
                xInputField.grid(column=1, row=i + 3)
                xInputFields.append(xInputField)
        elif count < len(xInputFields):
            for i in range(len(xInputFields) - count):
                xInputField = xInputFields.pop()
                xInputField.grid_remove()

    countInputField = InputField(
        master=subFrame,
        title="Count",
        type=InputFieldType.Integer,
        minimum=1,
        maximum=9,
        text=str(len(MatrixTranspose(neuralNetwork.inputs))),
        onChange=onCountInputFieldChange,
    )
    countInputField.grid(column=1, row=2, sticky=N)