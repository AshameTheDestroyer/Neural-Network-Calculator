from tkinter import *

def SubFrame(master: Misc, title: str) -> None:
    Label(
        master=master,
        text=title,
    ).pack(fill=X, anchor=N)