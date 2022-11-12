import sys
import requests
from typing import Dict, Any

from notificat.base import Notificat


class SlackAPI(Notificat):
    def __init__(self, token:str):
        super().__init__()
        
        self.token = token
        
        
    def send(self, channelID:str, message:str) -> Dict[str, Any]:
        """Send message to channel.

        Args:
            channelID (str): Channel ID where to send message.
            message (str): The message that send to be the channel.
            
        Returns:
            Dict[str, Any]: Response to a request. If the request is successful, the value with key "ok" is "True".
        """
        response = requests.post("https://slack.com/api/chat.postMessage",
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {self.token}"},
                                 json={"text": message, "channel": channelID})        
        return response.json()
        
    
    def get_msg(self, channelID:str, max:int) -> Dict[str, Any]:
        """Get messages from the input channel.          
            If channel has not enough messages to get, The number of message what you get can be less then `max` value.

        Args:
            channelID (str): Channel ID where to get message.
            max (int): Maximum number of messages what you get.

        Returns:
            Dict[str, Any]: Response to a request. If the request is successful, the value with key "ok" is "True".
        """
        response = requests.get(f'https://slack.com/api/conversations.history?channel={channelID}&limit={max}',
                                headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {self.token}'})
        
        return response.json()
    
    
    def get_latest_msg(self, channelID:str) -> Dict[str, Any]:
        """Get last last message from input channel.
        
        Args:
            channelID (str):  Channel ID where to get message.

        Returns:
            Dict[str, Any]: Response to a request. If the request is successful, the value with key "ok" is "True".
        """
        response = requests.get(f'https://slack.com/api/conversations.history?channel={channelID}&limit=1',
                                 headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {self.token}'})        
        return response.json()
            
            
    def get_channel_list(self, max:int=1) -> Dict[str, Any]:
        """Get channel list.

        Args:
            max (int): Maximum number of channels to get. Defaults to 1.

        Returns:
            Dict[str, Any]: Response to a request. If the request is successful, the value with key "ok" is "True".
        """
        response = requests.get(f"https://slack.com/api/conversations.list?limit={max}",
                                headers={"Content-Type": "application/json",
                                         "Authorization": f"Bearer {self.token}"})        
        
        return response.json()    
    
            
        
        
                
            
        
        