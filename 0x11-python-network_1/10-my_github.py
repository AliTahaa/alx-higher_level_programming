#!/usr/bin/python3
""" takes your Github and uses the Github API to display your id """


import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/{}'.format(argv[1])
    req = requests.get(url,
                       auth=(argv[1], argv[2]))
    print(req.json().get('id'))
