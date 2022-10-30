from notificat.base import Notificat


class Slack(Notificat):
    def __init__(self):
        super().__init__()
        
    def send(self, message: str) -> None:
        return super().send(message)