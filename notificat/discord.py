from requests import Response

from notificat.base import Notificat
import requests
from typing import Dict, Any

class DiscordClient(Notificat):

    def __init__(self, token: str):
        super().__init__()

        self.token = token

    def send(self, channelID: str, message: str) -> Response:
        """Send message to channel.
        Args:
            channelID (str): Channel ID where to send message.
            message (str): The message that send to be the channel.

        Returns:
            Response: Response to a request. If the request is successful, The status code is 200. You can get the response content with .json() method.
        """
        return requests.post(f"https://discord.com/api/channels/{channelID}/messages",
                                 headers={"Content-Type": "application/json", "Authorization": f"Bot {self.token}"},
                                 json={"content": message})

    def get_channel_list(self, serverID:str) -> Response:
        """Get channel list in your server.
                Args:
                    serverID (str): Server ID where to get the channel list.

                Returns:
                    Response: Response to a request. If the request is successful, The status code is 200. You can get the response content with .json() method.
                """
        return requests.get(f"https://discord.com/api/guilds/{serverID}/channels",
                            headers={"Content-Type": "application/json", "Authorization": f"Bot {self.token}"})

    def get_msg(self, channelID:str, max:int=None) -> Response:
        """Get Message in your Channel
                Args:
                    channelID (str): Channel ID where to get message.
                    max (int): The message counts which you want to get. if max = 1, this method is same with get_latest

                Returns:
                    Response: Response to a request. If the request is successful, The status code is 200. You can get the response content with .json() method.
                """
        url = f"https://discord.com/api/channels/{channelID}/messages"

        if max is not None:
            url += f"?limit={max}"

        return requests.get(url, headers={"Content-Type": 'application/json', "Authorization": f"Bot {self.token}"})

    def get_latest(self, channelID:str) -> Response:
        """Get The Latest Message in your channel
                Args:
                    channelID (str): Channel ID where to send message.

                Returns:
                    Response: Response to a request. If the request is successful, The status code is 200. You can get the response content with .json() method.
                """
        return requests.get(f"https://discord.com/api/channels/{channelID}/messages?limit=1",
                                 headers={"Content-Type": "application/json", "Authorization": f"Bot {self.token}"})
