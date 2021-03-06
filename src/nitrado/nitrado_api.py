from nitrado.client import Client
from nitrado.game_server import GameServer
from nitrado.service import Service
import requests
from requests import RequestException
import os


def assert_success(response):
    if not response:
        return
    if 'status' not in response or response['status'] != 'success':
        raise AssertionError(f"API returned: {response}")


class NitradoAPI:
    NITRADO_API_URL = "https://api.nitrado.net/"
    CLIENT = Client.CLIENT

    @classmethod
    def initialize_client(cls, key=None, url=None):
        if not (Client.CLIENT or GameServer.CLIENT or Service.CLIENT or NitradoAPI.CLIENT):
            key = key or os.getenv("NITRADO_KEY")
            url = url or NitradoAPI.NITRADO_API_URL
            assert key and url, f"The url and api key must be provided: url=>{url}, key=>{key}"
            client = Client(url, key)
            Client.CLIENT = client
            GameServer.CLIENT = client
            Service.CLIENT = client
            NitradoAPI.CLIENT = client

    def __init__(self, key=None, url=None):
        NitradoAPI.initialize_client(key, url)
        self.services = Service.all()
        self.game_servers = GameServer.all()

    def health_check(self):
        resp = NitradoAPI.CLIENT.get('ping')
        assert_success(resp)
        return resp['message']

    def maintenance_status(self):
        resp = NitradoAPI.CLIENT.get('maintenance')
        assert_success(resp)
        return resp['data']['maintenance']

    def version(self):
        resp = NitradoAPI.CLIENT.get('version')
        assert_success(resp)
        return resp['message']
