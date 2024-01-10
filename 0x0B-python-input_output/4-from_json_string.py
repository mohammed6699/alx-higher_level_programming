#!/usr/bin/python3
"""dserialization process"""

import json

def from_json_string(my_str):
    """convertion from json to object"""
    return json.loads(my_str)
