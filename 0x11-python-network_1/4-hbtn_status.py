#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
import requests

if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body Response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- type: {}".format(r.text))
