#!/usr/bin/python3
""" sends a POST request to the passed URL with the
    email as a parameter
"""

if __name__ == "__main__":
    import urllib.request
    import sys
    try:
        url = sys.argv[1]
        values = {"email": sys.argv[2]}
        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            request = response.read().decode('utf-8')
            print(request)
    except:
        pass
