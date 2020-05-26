#!/usr/bin/python3
"""
Hodor - Hbtn project

Level 0: HTTP request with parameters

Usage: python3 requester_0.py [id]

Author: @exploitpnk
"""
import requests
import sys

if len(sys.argv) == 2:
    url = "http://158.69.76.135/level0.php"
    user_id = sys.argv[1]
    data = {
        "id": user_id,
        "holdthedoor": "Submit+Query"
        }
    for i in range(1, 1024):
        response = requests.post(url=url, data=data)
        print("[#] Request", i, "sent: HTTP code:", response.status_code)
else:
    print("Usage: python3", sys.argv[0], "[id]")