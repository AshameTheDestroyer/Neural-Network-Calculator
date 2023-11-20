from typing import Callable

class Event():
    _subscribers: list[Callable]

    def __init__(self) -> None:
        self._subscribers = []

    def Subscribe(self, callback: Callable) -> None:
        self._subscribers.append(callback)

    def Unsubscribe(self, callback: Callable) -> None:
        try: self._subscribers.remove(callback)
        except: None

    def Fire(self, *args) -> None:
        for subscriber in self._subscribers:
            subscriber(*args)