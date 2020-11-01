#!/usr/bin/python3
""" Write a Python script that takes your Github credentials
    (username and password) and uses the Github API to display
    your id
 """

if __name__ == "__main__":
    from requests import get, auth
    import sys
    user = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    r = get(url, auth=auth.HTTPBasicAuth(user, password))
    try:
        js = r.json()
        print(js.get('id'))
    except ValueError:
        print("Not a valid JSON")
