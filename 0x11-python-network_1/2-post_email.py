#!/usr/bin/python3
""" Sends a POST request And displays the body """


import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    d = urllib.parse.urlencode(val).encode("ascii")

    request = urllib.request.Request(url, d)
    with urllib.request.urlopen(request) as resp:
        print(resp.read().decode("utf-8"))
