from tkinter import *
from tkinter.font import *

def TitledFrame(master: Misc, title: str) -> Frame:
    label = Label(
        master=master,
        text=title,
        font=("TkDefaultFont", 12, BOLD)
    )
    label.grid(column=1, row=1, sticky=EW, pady=(0, 10))

    subFrame = Frame(
        master=master,
    )
    subFrame.grid(column=1, row=2)
    subFrame.rowconfigure(index=1, weight=1)
    subFrame.columnconfigure(index=1, weight=1)

    return subFrame