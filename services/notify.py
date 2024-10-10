import requests


class Notify:

    def __init__(self):
      self.__base_url = 'https://webhook.site'

    def send_event(self, data):
      requests.post(
        url=f'{self.__base_url}/47c06982-b7b2-4c20-9e6b-62ed25ee424f',
        json=data,
      )

