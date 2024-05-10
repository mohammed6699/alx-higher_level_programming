#!/usr/bin/pyton3

import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]

    x = reauests.get(url)
    print(x.headers.get("X-Request-Id"))
