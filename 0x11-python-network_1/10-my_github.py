#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
uses the GitHub API to display your id
"""
import sys
import requests

if __name__ == "__main__":
    url = "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"
    params = {"search": sys.argv[1]}
    results = requests.get(url, params=params).json()

    print("number of results is: {}".format(results.get("count")))
    [print(r.get(name)) for r in results.get("results")]
