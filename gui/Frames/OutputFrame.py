from tkinter import *

from lib.classes.Matrix import *
from gui.lib.InputField import *
from gui.Frames.TitledFrame import *

from main import neuralNetwork

def OutputFrame(master: Misc) -> None:
    subFrame = TitledFrame(
        master=master,
        title="Output",
    )

    yInputFieldFrame = Frame(
        master=subFrame,
    )
    yInputFieldFrame.pack(expand=1)

    buttonFrame = Frame(
        master=subFrame,
    )
    buttonFrame.pack()

    calculateButton = Button(
        master=buttonFrame,
        text="Calculate",
        cursor="hand1",
        command=lambda: neuralNetwork.calculate(),
    )
    calculateButton.pack(expand=1, pady=(10, 0))

    yInputFields: list[InputField] = []

    def onOutputAltered(dimensionIndex: int, dimensionValue: tuple[int, int], weight: Matrix) -> None:
        if dimensionIndex != len(neuralNetwork.dimensions) - 1: return
        setYInputFieldCount(count=dimensionValue[0])

    def onOutputCalculated(output: Matrix) -> None:
        for i in range(len(yInputFields)):
            yInputFields[i].textVariable.set(str(output[i][0]))

    neuralNetwork.onDimensionAltered.Subscribe(onOutputAltered)
    neuralNetwork.onNetworkCalculated.Subscribe(onOutputCalculated)

    def setYInputFieldCount(count: int) -> None:
        if count > len(yInputFields):
            for i in range(len(yInputFields), count):
                yInputField = InputField(
                    master=yInputFieldFrame,
                    title="y" + str(i + 1).zfill(2),
                    type=InputFieldType.Float,
                    minimum=-10000,
                    maximum=10000,
                    state=InputFieldState.Readonly,
                    text=str(neuralNetwork.outputs[i]),
                )
                yInputField.grid(column=1, row=i + 1)
                yInputFields.append(yInputField)
        elif count < len(yInputFields):
            for i in range(len(yInputFields) - count):
                yInputField = yInputFields.pop()
                yInputField.grid_remove()
    
    setYInputFieldCount(count=len(neuralNetwork.outputs))

    neuralNetwork.onDimensionPopped.Subscribe(
        lambda: setYInputFieldCount(count=neuralNetwork.dimensions[-1][0]))