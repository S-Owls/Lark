from abc import ABCMeta, abstractmethod

class Notificat(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def send(self, message: str) -> None:
        pass
