#!/usr/bin/python3
""" Sends a request to the URL and displays the body of the response """


import requests
from sys import argv

if __name__ == '__main__':
    req = requests.get(argv[1])
    status = req.status_code
    txt = req.text
    print(txt) if status < 400 else print(
        "Error code: {}".format(req.status_code))
