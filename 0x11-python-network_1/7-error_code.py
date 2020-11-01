#!/usr/bin/python3
""" Sends a request to the URL and displays the
    body of the response.
"""

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    response = requests.get(url)
    code = response.status_code
    if (code >= 400):
        print("Error code: {}".format(code))
    else:
        print(response.text)
