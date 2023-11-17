from tkinter import *

from FrameArray import *

window = Tk()
window.title("Neural Network Calculator")

mainFramePadding = 20
mainFrame = Frame(
    master=window,
    padx=mainFramePadding,
    pady=mainFramePadding,
)

mainFrame.pack(fill=BOTH, expand=1)

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
        frame.grid(column=j, row=i, sticky=NSEW)

        frameArray[i][j](frame)

window.mainloop()