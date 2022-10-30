from abc import ABC


class Notifier(ABC):

    def __init__(self):
        pass

    def send(self, message: str) -> None:
        pass
