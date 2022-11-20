import sys
import requests
from typing import Dict, Any

from notificat.base import Notificat


class SlackAPI(Notificat):
    def __init__(self, token:str):
        super().__init__()
        
        self.token = token
        
        
    def send(self, channelID:str, message:str) -> requests.Response:
        """Send message to channel.

        Args:
            channelID (str): Channel ID where to send message.
            message (str): The message that send to be the channel.
            
        Returns:
            requests.Response: Response to a request.
        """
      
        return requests.post("https://slack.com/api/chat.postMessage",
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {self.token}"},
                                 json={"text": message, "channel": channelID})        
        
    
    def get_msg(self, channelID:str, max:int) -> requests.Response:
        """Get messages from the input channel.          
            If channel has not enough messages to get, The number of message what you get can be less then `max` value.

        Args:
            channelID (str): Channel ID where to get message.
            max (int): Maximum number of messages what you get.

        Returns:
            requests.Response: Response to a request.
        """
        
        return requests.get(f'https://slack.com/api/conversations.history?channel={channelID}&limit={max}',
                                headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {self.token}'})
    
    
    def get_latest_msg(self, channelID:str) -> requests.Response:
        """Get last last message from input channel.
        
        Args:
            channelID (str):  Channel ID where to get message.

        Returns:
            requests.Response: Response to a request.
        """
       
        return requests.get(f'https://slack.com/api/conversations.history?channel={channelID}&limit=1',
                                 headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {self.token}'})      
            
            
    def get_channel_list(self, max:int=None) -> requests.Response:
        """Get channel list.

        Args:
            max (int): Maximum number of channels to get. Defaults to 1.

        Returns:
            requests.Response: Response to a request.
        """
        url = f"https://slack.com/api/conversations.list"
        
        if max is not None:
            url += f"?limit={max}"
                        
        return requests.get(url, headers={"Content-Type": "application/json", "Authorization": f"Bearer {self.token}"})        
    
            
        
        
                
            
        
        