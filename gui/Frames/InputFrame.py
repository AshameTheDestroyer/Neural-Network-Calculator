from tkinter import *

from lib.InputField import *
from Frames.TitledFrame import *

def InputFrame(master: Misc) -> None:
    subFrame = TitledFrame(
        master=master,
        title="Input",
    )

    xInputFields: list[InputField] = []

    def countInputFieldOnChange(mode: TextChangeMode, text: str) -> None:
        if mode != TextChangeMode.onWrite: return
        
        count = int(text)
        if count > len(xInputFields):
            for i in range(len(xInputFields), count):
                xInputField = InputField(
                    master=subFrame,
                    title="x" + str(i + 1).zfill(2),
                    type=InputFieldType.Integer,
                    minimum=-100,
                    maximum=100,
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
        onChange=countInputFieldOnChange,
        type=InputFieldType.Integer,
        minimum=3,
        maximum=10,
    )
    countInputField.grid(column=1, row=2, sticky=N)