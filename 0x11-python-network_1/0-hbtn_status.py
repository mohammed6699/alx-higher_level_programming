#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request
if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body Response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(type(body)))
        print("\t- utf8 content: {}".format(type(body.decode("utf-8"))))
