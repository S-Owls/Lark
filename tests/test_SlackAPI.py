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
    
    def test_check_empty_token(self):
        self.assertFalse(len(self.token)==0)
        
    def test_check_empty_ch_id(self):
        self.assertFalse(len(self.ch_id)==0)    
    
    def test_send(self):
        now = datetime.datetime.now()
        #str_now = now.strftime('%Y-%m-%d %H:%M:%S')
        try:
            self.slackAPI.send("test", f"{now.strftime('%Y-%m-%d %H:%M:%S')} [unittest] SlackAPI.send()")
        except Exception as e:
            print(e)
            
    