#!/usr/bin/python3

import sys
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

arglist = list(sys.argv[1:])
try:
    old_d = load_from_json_file('add_item.json')
except Exception:
    old_d = []

old_d.extend(arglist)
save_to_json_file(old_d, add_item.json)
