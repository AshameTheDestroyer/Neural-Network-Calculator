from tkinter import *
from tkinter.ttk import *

def TabComponent(master: Misc, tabs: list[str]) -> list[Frame]:
    notebook = Notebook(
        master=master,
    )
    notebook.grid(column=1, row=1, sticky=NSEW)

    tabFrames: list[Frame] = []
    for i in range(len(tabs)):
        tab = Frame(
            master=notebook,
        )
        notebook.add(child=tab, text=tabs[i])
        tabFrames.append(tab)
    
    return tabFrames