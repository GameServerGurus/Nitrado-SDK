import requests
from requests import RequestException

class ArkAPI:
    @classmethod
    def unofficial_server_list(cls):
        req = requests.get("http://arkdedicated.com/xbox/cache/unofficialserverlist.json")
        if not req.ok:
            code = req.status_code
            reason = req.reason
            raise RequestException(f"Url error => {code} {reason} for:", req.url)
        return req.json()

    @classmethod
    def official_server_list(cls):
        req = requests.get("http://arkdedicated.com/xbox/cache/officialserverlist.json")
        if not req.ok:
            code = req.status_code
            reason = req.reason
            raise RequestException(f"Url error => {code} {reason} for:", req.url)
        return req.json()

    @classmethod
    def banned_list(cls):
        req = requests.get("http://arkdedicated.com/xboxbanlist.txt")
        return req.text.split('\r\n')