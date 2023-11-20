from tkinter import *
from tkinter.ttk import *

import matplotlib.pyplot as plotter

from gui.Frames.TitledFrame import *
from lib.classes.ActivationFunctions import *

from main import neuralNetwork

def ActivationFunctionFrame(master: Misc) -> None:
    subFrame = TitledFrame(
        master=master,
        title="Activation Function",
    )

    activationFunctions = [
        activationFunction for activationFunction in vars(ActivationFunctions)
        if activationFunction[0] != "_"
    ]

    multiclassActivationFunctions = [
        activationFunction for activationFunction in vars(MulticlassActivationFunctions)
        if activationFunction[0] != "_"
    ]

    def onComboboxChange(value: str) -> None:
        try:
            neuralNetwork.activationFunction = \
                ActivationFunctions.__getattribute__(ActivationFunctions, value)
            neuralNetwork.multiclassActivationFunction = None
        except:
            neuralNetwork.activationFunction = None
            neuralNetwork.multiclassActivationFunction = \
                MulticlassActivationFunctions.__getattribute__(MulticlassActivationFunctions, value)

    comboboxTextVariable = StringVar(value=activationFunctions[0])
    comboboxTextVariable.trace_add("write", lambda var, index, mode: mode == "write" and onComboboxChange(comboboxTextVariable.get()))
    
    combobox = Combobox(
        master=subFrame,
        values=activationFunctions,
        state="readonly",
        textvariable=comboboxTextVariable,
    )
    combobox.grid(column=1, row=1, sticky=NSEW)

    radioButtonFrame = Frame(
        master=subFrame,
    )
    radioButtonFrame.grid(column=1, row=2, sticky=NSEW, pady=10)

    graphButton: Button

    def setComboboxValues(values: list[str], disableGraphButton: bool = False) -> None:
        combobox["values"] = values
        comboboxTextVariable.set(values[0])
        graphButton["state"] = DISABLED if disableGraphButton else NORMAL
        graphButton["cursor"] = "" if disableGraphButton else "hand1"

    radioButtons = [
        {
            "title": "Regular",
            "command": lambda: setComboboxValues(activationFunctions),
        },
        {
            "title": "Multiclass",
            "command": lambda: setComboboxValues(multiclassActivationFunctions, disableGraphButton=True),
        },
    ]

    for i in range(len(radioButtons)):
        radioButton = Radiobutton(
            master=radioButtonFrame,
            text=radioButtons[i]["title"],
            value=radioButtons[i]["title"],
            command=radioButtons[i]["command"],
        )
        radioButton.grid(column=i + 1, row=1)
        if i == 0: radioButton.select()

    limit, modifier = 1000, 100

    def graphActivationFunction() -> None:
        (activationFunctionName, activationFunction) = list(filter(
                lambda item: item[0] == comboboxTextVariable.get(),
                vars(ActivationFunctions).items()
        ))[0]

        xs = [x / modifier for x in range(-limit, limit + 1)]
        ys = [activationFunction(x / modifier) for x in range(-limit, limit + 1)]

        plotter.title(activationFunctionName)
        plotter.plot(xs, ys)
        plotter.ylim(-limit / modifier, (limit + 1) / modifier)
        plotter.grid(True)
        plotter.show(block=True)

    def clearGraph() -> None:
        plotter.title("None")
        plotter.clf()
        plotter.ylim(-limit / modifier, (limit + 1) / modifier)
        plotter.grid(True)
        plotter.show(block=True)

    buttonFrame = Frame(
        master=subFrame,
    )
    buttonFrame.grid(column=1, row=3, sticky=NSEW)

    graphButton = Button(
        master=buttonFrame,
        text="Graph Activation Function",
        cursor="hand1",
        command=graphActivationFunction,
    )
    graphButton.grid(column=1, row=1, sticky=NSEW)

    clearButton = Button(
        master=buttonFrame,
        text="Clear Graph",
        cursor="hand1",
        command=clearGraph,
    )
    clearButton.grid(column=2, row=1, sticky=NSEW)