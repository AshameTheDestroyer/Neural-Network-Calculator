from tkinter import *
from tkinter.ttk import *

def TabComponent(master: Misc, tabs: list[str]) -> tuple[Notebook, list[Frame]]:
    notebook = Notebook(
        master=master,
    )

    tabFrames: list[Frame] = []
    for i in range(len(tabs)):
        tab = Frame(
            master=notebook,
        )
        notebook.add(child=tab, text=tabs[i])
        tabFrames.append(tab)
    
    return (notebook, tabFrames)