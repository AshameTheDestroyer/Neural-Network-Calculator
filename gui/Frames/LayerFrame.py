from tkinter import *
from tkinter.ttk import *

from gui.lib.InputField import *
from gui.lib.TabComponent import *

def LayerFrame(master: Misc) -> Frame:
    subFrame = Frame(
        master=master,
    )

    layerCount: int
    def inputFieldOnChange(mode: TextChangeMode, text: str):
        if mode == TextChangeMode.onWrite:
            layerCount = int(text)

    InputField(
        master=subFrame,
        type=InputFieldType.Integer,
        minimum=1,
        maximum=10,
        title="Layer Count",
        onChange=inputFieldOnChange,
    )

    # add

    TabComponent(
        master=master,
        tabs=["Layer" + str(i + 1).zfill(2) for i in range(layerCount)],
    )

    return subFrame