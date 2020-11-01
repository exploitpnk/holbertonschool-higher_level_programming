#!/usr/bin/python3
""" Displays the value of the X-Request-Id variable """

if __name__ == "__main__":
    import urllib.request
    import sys
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            request = response.info().get('X-Request-Id')
            print(request)

    except:
        pass
