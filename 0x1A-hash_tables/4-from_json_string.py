#!/usr/bin/python3
# 6-from_json_string.py
"""Defines JSON to- object func"""
import json


def from_json_string(my_str):
    """Return Python object representation of JSON stri"""
    return json.loads(my_str)
