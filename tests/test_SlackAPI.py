import os
import datetime
from unittest import TestCase

from notificat import SlackAPI


class Test_SlackAPI(TestCase):
    def setUp(self):
        if os.path.isfile(".env"):
            from dotenv import load_dotenv
            load_dotenv()
        
        self.token = os.environ["SLACK_TOKEN"]
        self.ch_id = os.environ["SLACK_TEST_CH_ID"]
        
        self.slackAPI = SlackAPI(self.token)
        
        self.now = datetime.datetime.now()
    
    
    def test_check_empty_token(self):
        self.assertFalse(len(self.token)==0)
        
        
    def test_check_empty_ch_id(self):
        self.assertFalse(len(self.ch_id)==0)    
    
    
    def test_send(self):       
        response = self.slackAPI.send(self.ch_id, f"{self.now.strftime('%Y-%m-%d %H:%M:%S')} [unittest] SlackAPI.send()")
        self.assertTrue(response.json()["ok"])
        
        
    def test_get_msg(self):
        response = self.slackAPI.get_msg(self.ch_id, 5)
        self.assertTrue(response.json()["ok"])
    
            
    def test_get_latest_msg(self):
        response = self.slackAPI.get_latest_msg(self.ch_id)
        self.assertTrue(response.json()["ok"])
        
        
    def test_get_channel_list(self):
        response = self.slackAPI.get_channel_list(5)
        self.assertTrue(response.json()["ok"])
