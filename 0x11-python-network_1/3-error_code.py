#!/usr/bin/python3
""" Displays the body of the response """

if __name__ == "__main__":
    from urllib.request import urlopen
    from urllib.error import HTTPError
    import sys
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            body_response = response.read().decode('utf-8')
            print(body_response)

    except HTTPError as e:
        print('Error code: {}'.format(e.code))
