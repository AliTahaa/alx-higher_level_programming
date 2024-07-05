#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """


import requests

if __name__ == '__main__':
    url = "https://intranet.hbtn.io/status"
    req = requests.get(url)
    text = req.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
