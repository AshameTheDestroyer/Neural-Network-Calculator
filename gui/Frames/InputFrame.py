from tkinter import *

from lib.InputField import *
from Frames.SubFrame import *

def InputFrame(master: Misc):
    SubFrame(
        master=master,
        title="Input",
    )

    InputField(
        master=master,
        title="Count",
        onChange=lambda mode, text: mode == TextChangeMode.onWrite and print(text),
        type=InputFieldType.Integer,
        minimum=3,
        maximum=10,
    ).pack()