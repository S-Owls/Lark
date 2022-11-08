import sys
import requests
from typing import overload, Dict

from notificat.base import Notificat


class Slack(Notificat):
    def __init__(self, token:str):
        super().__init__()
        
        self.token = token
        
        
    def send(self, channelID:str, message:str):
        """Send message to channel.

        Args:
            channelID (str): Channel ID where to send message.
            message (str): The message that send to be the channel.
        """
        response = requests.post("https://slack.com/api/chat.postMessage",
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {self.token}"},
                                 json={"text": message, "channel": channelID})
        
        self.check_error(response)
        
    # TO DO:
    def get_msg(self, channelID:str, max:int):
        pass
    
    # TO DO:
    def get_latest_msg(self, channelID:str, max:int):
        pass
            
            
    def get_channel_list(self, max:int=1) -> Dict[str, str]:
        """Get channel list.

        Args:
            max (int): Maximum number of channels to get. Defaults to 1.

        Returns:
            Dict[str, str]: The return value that channel list. 
                        Output dictionary shape like: {"id":"name"}.
        """
        response = requests.get(f"https://slack.com/api/conversations.list?limit={max}",
                                headers={"Content-Type": "application/json",
                                         "Authorization": f"Bearer {self.token}"})        
        
        self.check_error(response)
        
        return {c["id"]:c["name"] for c in response.json()["channels"]}
        
        
    def check_error(self, response:requests.Response):
        """Check any error from ``requests.Response`` object.

        Args:
            response (requests.Response): Reesult object of ``requests.get()`` and ``requests.post()``.

        Raises:
            Exception: When ``GET/POST`` message get an ``status_code`` other than 200.
                    Or get ``false`` response with error message from slack api.
        """
        method_name = sys._getframe(1).f_code.co_name
        
        if not response.status_code == 200:
            print(f"[Error] func:Slack.{method_name} - Faild to get response from API(ok code != 200)")
            raise Exception("[Error] Faild to get response from API(ok code != 200)")
        
        response = response.json()
        if not response["ok"]:
            print(f"[Error] func:Slack.{method_name} - {response}")
            
            # TO DO:
            # Determining the error message
            raise Exception("[Error] Failed to GET/POST ~~.")
            
        
        
                
            
        
        