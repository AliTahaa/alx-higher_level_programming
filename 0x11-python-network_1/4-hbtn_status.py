#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status """


import requests

if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url)
    txt = req.text
    print("Body response:")
    print("\t- type: {}".format(type(txt)))
    print("\t- content: {}".format(txt))
