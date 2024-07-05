#!/usr/bin/python3
""" Sends a request to the URL And displays the value """


import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as responce:
        print(dict(responce.headers).get("X-Request-Id"))
