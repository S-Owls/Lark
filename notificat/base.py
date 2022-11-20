from abc import ABCMeta, abstractmethod
import requests

class Notificat(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def send(self, channelID: str, message: str) -> requests.Response:
        pass

