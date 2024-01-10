#!/usr/bin/python3
"""creates object from json"""

import json
def load_from_json_file(filename):
    """ function that creates an Object from a JSON file"""
    def load_from_json_file(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
