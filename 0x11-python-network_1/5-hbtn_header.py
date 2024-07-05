#!/usr/bin/python3
""" Sends a request to the URL and displaysthe value of the variable """


import requests
from sys import argv

if __name__ == '__main__':
    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))
