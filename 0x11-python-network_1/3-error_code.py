#!/usr/bin/python3
""" Send a request to URL and dispaly body """


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as responce:
            print(responce.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
