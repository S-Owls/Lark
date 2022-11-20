import os
import datetime
from unittest import TestCase

from notificat import DiscordClient

class Test_Discord(TestCase):
    def setUp(self):
        if os.path.isfile(".env"):
            from dotenv import load_dotenv
            load_dotenv()

        self.token = os.environ["DISCORD_TOKEN"]
        self.ch_id = os.environ["DISCORD_TEST_CH_ID"]
        self.server_id = os.environ["DISCORD_SERVER_ID"]

        self.discordClient = DiscordClient(self.token)

        self.now = datetime.datetime.now()

    def test_check_empty_token(self):
        self.assertFalse(len(self.token) == 0)

    def test_check_empty_ch_id(self):
        self.assertFalse(len(self.ch_id) == 0)

    def test_send(self):
        response = self.discordClient.send(self.ch_id,
                                      f"{self.now.strftime('%Y-%m-%d %H:%M:%S')} [unittest] SlackAPI.send()")

        self.assertTrue(response.status_code, 200)

    def test_get_channel_list(self):
        response = self.discordClient.get_channel_list(self.server_id)

        self.assertTrue(response.status_code, 200)

    def test_get_msg(self):
        response = self.discordClient.get_msg(self.ch_id,3)

        self.assertTrue(response.status_code, 200)

    def test_get_latest(self):
        response = self.discordClient.get_latest(self.ch_id)

        self.assertTrue(response.status_code, 200)

