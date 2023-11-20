from tkinter import *
from tkinter.font import *
from typing import Callable

from gui.FrameArray import *

window = Tk()
window.title("Neural Network Calculator")

defaultFont = nametofont("TkDefaultFont")
defaultFont.configure(family="Cascadia Code")
window.option_add("*Font", defaultFont)

mainFramePadding = 20
mainFrame = Frame(
    master=window,
    padx=mainFramePadding,
    pady=mainFramePadding,
)

mainFrame.pack(fill=BOTH, expand=1)

def render() -> None:
    framePadding = 10
    for i in range(len(frameArray)):
        mainFrame.columnconfigure(index=i, weight=1)
        for j in range(len(frameArray[i])):
            mainFrame.rowconfigure(index=j, weight=1)

            frame = Frame(
                master=mainFrame,
                border=2,
                padx=framePadding,
                pady=framePadding,
                relief=SUNKEN,
            )

            function: Callable
            rowspan: int = None
            columnspan: int = None
            if isinstance(frameArray[i][j], Callable):
                function = frameArray[i][j]
            else:
                function = frameArray[i][j]["function"]

                try: rowspan = frameArray[i][j]["rowspan"]
                except: None

                try: columnspan = frameArray[i][j]["columnspan"]
                except: None

            frame.grid(column=j, row=i, sticky=NSEW, rowspan=rowspan, columnspan=columnspan)
            frame.rowconfigure(index=2, weight=1)
            frame.columnconfigure(index=1, weight=1)
            function(frame)

    window.mainloop()

render()