from tkinter import *
from enum import Enum
from typing import Callable
from math import inf, isfinite

class TextChangeMode(Enum):
    onRead = "read"
    onWrite = "write"

class InputFieldType(Enum):
    String = "string"
    Integer = "integer"
    Float = "float"

class InputFieldState(Enum):
    Normal = "normal"
    Readonly = "readonly"
    Disabled = "disabled"

class InputFieldDisplay(Enum):
    Horizontal = "horizontal"
    Vertical = "vertical"

TextVariableOnChange = Callable[[TextChangeMode, str], None]

class InputField(Frame):
    label: Label
    entry: Entry
    textVariable: StringVar
    type: InputFieldType
    minimum: float
    maximum: float
    
    _previousTextValue: str
    _gap: int = 10
    _entryPadding: int = 1
    _isReadyToCallOnChange: bool = False

    def __init__(
        self,
        master: Misc,
        title: str,
        text: str = "",
        onChange: TextVariableOnChange = None,
        type: InputFieldType = InputFieldType.String,
        minimum: float = -inf,
        maximum: float = +inf,
        state: InputFieldState = InputFieldState.Normal,
        display: InputFieldDisplay = InputFieldDisplay.Horizontal,
    ) -> None:
        super().__init__(
            master=master,
        )

        self._setUpRange(minimum, maximum)
        self._setUpLabel(title, display)
        self._setUpTextVariable(text, onChange)
        self._setUpType(type, text)
        self._setUpEntry(state, display)

        if type != InputFieldType.String and state == InputFieldState.Normal:
            self._setUpButtons(display)

    def _setUpRange(self, minimum: float, maximum: float) -> None:
        if minimum > maximum:
            minimum, maximum = maximum, minimum

        self.minimum = minimum
        self.maximum = maximum

    def _setUpType(self, type: InputFieldType, text: str) -> None:
        self.type = type

        match type:
            case InputFieldType.Integer:
                text = text if (self._validateInteger(text)) else "0"
                text = str(int(self._clamp(int(text))))
            case InputFieldType.Float:
                text = text if (self._validateFloat(text)) else "0"
                text = str(self._clamp(float(text)))
        
        self._previousTextValue = text
        self.textVariable.set(text)

    def _setUpLabel(self, title: str, display: InputFieldDisplay) -> None:
        self.label = Label(
            master=self,
            text=title,
            justify=CENTER,
        )
        
        match display:
            case InputFieldDisplay.Horizontal:
                self.label.grid(column=1, row=1)
            case InputFieldDisplay.Vertical:
                self.label.grid(column=1, row=2)

    def _setUpTextVariable(self, text: str, onChange: TextVariableOnChange = None) -> None:
        self.textVariable = StringVar(master=self, value=text)
        
        def onWrite(var: str, index: str, mode: str) -> None:
            self._validateText()

            self._isReadyToCallOnChange ^= True
            if self._isReadyToCallOnChange:
                onChange and onChange(TextChangeMode.onWrite, self.textVariable.get())
        
        def onRead(var: str, index: str, mode: str) -> None:
            onChange and onChange(TextChangeMode.onRead, self.textVariable.get())

        self.textVariable.trace_add(mode="write", callback=onWrite)
        self.textVariable.trace_add(mode="read", callback=onRead)

    def _setUpEntry(self, state: InputFieldState, display: InputFieldDisplay) -> None:
        width: int = None

        if self.type != InputFieldType.String:
            minimum, maximum = self.minimum, self.maximum
            if isfinite(minimum) and isfinite(maximum):
                width = max(
                    len(str(minimum if minimum != -inf else 0)),
                    len(str(maximum if maximum != -inf else 0)),
                )
            if self.type == InputFieldType.Float:
                width += 1

        self.entry = Entry(
            master=self,
            textvariable=self.textVariable,
            justify="center",
            width=width + InputField._entryPadding,
            state=state.value,
            disabledforeground="black",
        )

        padx = (InputField._gap, 0)
        ipady=InputField._entryPadding * 5 / 2

        match display:
            case InputFieldDisplay.Horizontal:
                self.entry.grid(column=2, row=1, padx=padx, ipady=ipady)
            case InputFieldDisplay.Vertical:
                self.entry.grid(column=1, row=1, padx=padx, ipady=ipady)
    
    def _validateInteger(self, text: str) -> bool:
        try:
            int(text)
            return True
        except:
            return False
        
    def _validateFloat(self, text: str) -> bool:
        try:
            float(text)
            return True
        except:
            return False
        
    def _clamp(self, number: int | float) -> float:
        return \
            self.minimum if (self.minimum > number) else \
            self.maximum if (self.maximum < number) else number
    
    def _setUpButtons(self, display: InputFieldDisplay) -> None:
        buttonFrame = Frame(
            master=self,
        )
        match display:
            case InputFieldDisplay.Horizontal:
                buttonFrame.grid(column=3, row=1)
            case InputFieldDisplay.Vertical:
                buttonFrame.grid(column=2, row=1)
                                
        def incrementButton(amount: int | float) -> None:
            value = str(self._getValue() + amount)
            self.textVariable.set(value)
            self._validateText()

        buttons = [
            {
                "text": "⤊",
                "command": lambda: incrementButton(+1),
            },
            {
                "text": "⤋",
                "command": lambda: incrementButton(-1),
            },
        ]

        for i in range(len(buttons)):
            buttonSize = 25
            buttonSubFrame = Frame(
                master=buttonFrame,
                width=buttonSize,
                height=buttonSize / 2,
            )
            buttonSubFrame.grid_propagate(False)
            buttonSubFrame.columnconfigure(0, weight=1)
            buttonSubFrame.rowconfigure(0, weight=1)
            buttonSubFrame.grid(column=1, row=i + 1)

            Button(
                master=buttonSubFrame,
                text=buttons[i]["text"],
                padx=0,
                pady=0,
                command=buttons[i]["command"],
                cursor="hand1",
            ).grid(sticky=NSEW)
    
    def _getIntegerValue(self) -> int:
        if self.type != InputFieldType.Integer:
            raise TypeError("Input field type is not an integer.")
        return int(self.textVariable.get())
    
    def _getFloatValue(self) -> float:
        if self.type != InputFieldType.Float:
            raise TypeError("Input field type is not a float.")
        return float(self.textVariable.get())
    
    def _getValue(self) -> str | int | float:
        match self.type:
            case InputFieldType.String: return self.textVariable.get()
            case InputFieldType.Integer: return self._getIntegerValue()
            case InputFieldType.Float: return self._getFloatValue()
    
    def _validateText(self) -> None:
        text = self.textVariable.get()

        match self.type:
            case InputFieldType.Integer:
                if not self._validateInteger(text):
                    self.textVariable.set(self._previousTextValue)
                    return
                
                text = str(int(self._clamp(int(text))))
                self._previousTextValue = text
                self.textVariable.set(text)
                    
            case InputFieldType.Float:
                if not self._validateFloat(text):
                    self.textVariable.set(self._previousTextValue)
                    return
                
                text = str(self._clamp(float(text)))
                self._previousTextValue = text
                self.textVariable.set(text)