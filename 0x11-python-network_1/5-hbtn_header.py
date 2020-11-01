#!/usr/bin/python3
""" Displays the value of the variable X-Request-Id """

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    r = requests.get(url)
    request = r.headers.get('X-Request-Id')
    print(request)
