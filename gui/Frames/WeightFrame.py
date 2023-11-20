from tkinter import *
from tkinter.ttk import *

from lib.classes.Matrix import *
from gui.lib.InputField import *
from gui.lib.TabComponent import *
from gui.Frames.TitledFrame import *
from lib.classes.MatrixElement import *
from lib.functions.MatrixOperations.MatrixPrinting import *
from lib.functions.MatrixOperations.MatrixTranspose import *

from main import neuralNetwork

def WeightFrame(master: Misc) -> None:
    subFrame = TitledFrame(
        master=master,
        title="Weights",
    )
    subFrame.grid(column=1, row=2, sticky=NSEW)
    
    buttonFrame = Frame(
        master=subFrame,
    )
    buttonFrame.pack()

    def onLayerCountInputFieldChange(mode: TextChangeMode, value: str) -> None:
        if mode != TextChangeMode.onWrite: return
        
        count = int(value)
        if count > len(neuralNetwork.weights):
            for i in range(len(neuralNetwork.weights), count):
                neuralNetwork.appendDimension(1)
        elif count < len(neuralNetwork.weights):
            for i in range(len(neuralNetwork.weights) - count):
                neuralNetwork.popDimension()

    layerCountInputField = InputField(
        master=buttonFrame,
        title="Layer Count",
        minimum=1,
        maximum=9,
        type=InputFieldType.Integer,
        text=str(len(neuralNetwork.weights)),
        onChange=onLayerCountInputFieldChange,
    )
    layerCountInputField.pack(anchor=CENTER)

    (notebook, layerTabs) = TabComponent(
        master=subFrame,
        tabs=["Layer" + str(i + 1).zfill(2) for i in range(len(neuralNetwork.weights))],
    )
    notebook.pack(fill=BOTH, expand=1)

    layerSubFrames: list[Frame] = []
    wInputFields: list[list[list[InputField]]] = [[] for layerTab in layerTabs]

    def onLayerCountIncrement(lastWeight, output) -> None:
        layerTab = Frame(
            master=notebook,
        )
        notebook.add(child=layerTab, text="Layer" + str(len(layerTabs) + 1).zfill(2))
        layerTabs.append(layerTab)
        wInputFields.append([])
        renderLayer(len(layerTabs) - 1)
    
    def onLayerCountDecrement() -> None:
        poppedLayerTab = layerTabs.pop()
        notebook.forget(poppedLayerTab)
        poppedLayerTab.grid_remove()

        layerSubFrames.pop()
        wInputFields.pop()

    neuralNetwork.onDimensionAppended.Subscribe(onLayerCountIncrement)
    neuralNetwork.onDimensionPopped.Subscribe(onLayerCountDecrement)

    def onWeightAltered(dimensionIndex: int, dimensionValue: tuple[int, int], weight: Matrix) -> None:
        if dimensionIndex == 0 or dimensionIndex == len(neuralNetwork.dimensions) - 1: return

        clearLayer(dimensionIndex - 1)
        displayLayer(dimensionIndex - 1)

    def displayLayer(layerIndex: int) -> None:
        if layerIndex >= len(layerSubFrames): return

        for i in range(len(neuralNetwork.weights[layerIndex])):
            layerSubFrames[layerIndex].rowconfigure(i, weight=1)

            wInputFields[layerIndex].append([])
                
            for j in range(len(neuralNetwork.weights[layerIndex][i])):
                layerSubFrames[layerIndex].columnconfigure(j, weight=1)

                def onWeightInputFieldChange(mode: TextChangeMode, value: str, i = i, j = j) -> None:
                    if mode != TextChangeMode.onWrite: return
                    neuralNetwork.weights[layerIndex][i][j] = float(value)

                wInputField = InputField(
                    master=layerSubFrames[layerIndex],
                    minimum=-100,
                    maximum=100,
                    title=f"w{i + 1}{j + 1}",
                    type=InputFieldType.Float,
                    text=str(neuralNetwork.weights[layerIndex][i][j]),
                    display=InputFieldDisplay.Vertical,
                    onChange=onWeightInputFieldChange,
                )
                wInputField.grid(row=i, column=j, padx=3, pady=3)

                wInputFields[layerIndex][i].append(wInputField)
    
    def clearLayer(layerIndex: int) -> None:
        for i in range(len(wInputFields[layerIndex])):
            for j in range(len(wInputFields[layerIndex][i])):
                wInputFields[layerIndex][i][j].grid_remove()

    neuralNetwork.onDimensionAltered.Subscribe(onWeightAltered)

    def renderLayer(i: int) -> None:
        configurationFrame = Frame(
            master=layerTabs[i],
        )
        configurationFrame.pack()

        def onWeightWidthInputFieldChange(mode: TextChangeMode, text: str, i = i) -> None:
            if mode != TextChangeMode.onWrite: return
            
            count = int(text)
            neuralNetwork.alterDimension(i + 1, (len(neuralNetwork.weights[i]), count))

        weightWidthInputField = InputField(
            master=configurationFrame,
            minimum=1,
            maximum=9,
            title="Count",
            type=InputFieldType.Integer,
            text=str(len(MatrixTranspose(neuralNetwork.weights[i]))),
            onChange=onWeightWidthInputFieldChange,
        )
        weightWidthInputField.pack()

        subFrame = Frame(
            master=layerTabs[i],
        )
        subFrame.pack(expand=1)
        layerSubFrames.append(subFrame)
        displayLayer(i)

    for i in range(len(layerTabs)):
        renderLayer(i)