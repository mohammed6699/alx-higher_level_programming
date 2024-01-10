#!/usr/bin/python3
"""writes an object to atext file"""

import json
def save_to_json_file(my_obj, filename):
    """writes an Object to a text file,"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
