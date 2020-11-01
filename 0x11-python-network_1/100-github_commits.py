#!/usr/bin/python3
""" Interview """

if __name__ == "__main__":
    from requests import get, auth
    import sys
    repo = sys.argv[1]
    user = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, repo)
    r = get(url)
    try:
        js_var = r.json()
        for j in js_var[:10]:
            author, name = None, None
            sha = j.get('sha')
            commit = j.get('commit')
            if commit:
                author = commit.get('author')
            if author:
                name = author.get('name')
            print("{}: {}".format(sha, name))
    except ValueError:
        print("Not a valid JSON")
