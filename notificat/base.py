from abc import ABC, abstractmethod


class Notificat(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def send(self, channelID: str, message: str) -> None:
        pass
