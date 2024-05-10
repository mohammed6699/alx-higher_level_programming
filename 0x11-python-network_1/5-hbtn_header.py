#!/usr/bin/pyton3

import sys
import requests
if __name__ == "__main__":
    r = sys.argv[1]

    x = reauests.get(r)
    print(x.headers.get("X-Request-Id"))
