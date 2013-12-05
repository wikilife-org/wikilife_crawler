# coding=utf-8

import base64
import requests


class TwitterAuth(object):

    _api_host = None

    def __init__(self, api_host):
        self._api_host = api_host

    def get_bearer_token(self, consumer_key, consumer_secret):
        bearer_token_credentials = base64.b64encode(consumer_key + ":" + consumer_secret)
        service_url = "/oauth2/token"
        url = self._api_host + service_url
        body = "grant_type=client_credentials"
        headers = {
            "User-Agent" : "wikilife_crawler",
            "Content-Length": "29",
            "Accept-Encoding": "gzip",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Authorization" : "Basic " + bearer_token_credentials
        }

        response = requests.request(method="POST", url=url, data=body, headers=headers)
        return response.content 


if __name__ == '__main__':

    consumer_key = "kV66a3p8Gd4cNcRk4wqVA"
    consumer_secret = "zAw1bVOCvWEPC397hGPC0q1ttNXLu8vAVDxnQWYjD4"

    print TwitterAuth('https://api.twitter.com').get_bearer_token(consumer_key, consumer_secret)
    #{"token_type":"bearer","access_token":"AAAAAAAAAAAAAAAAAAAAADN1RQAAAAAAmVtYyNrCtp59urnIfj5u1f5ZEV8%3DECQSxvLGArFNd0SqMtN7uoOLdmqf7A1prf0kzKYMGY"}
