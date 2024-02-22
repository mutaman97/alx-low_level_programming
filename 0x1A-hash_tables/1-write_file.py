#!/usr/bin/python3
"""Defines file_writing func"""


def write_file(filename="", text=""):
    """Write string to UTF8 text file

    Args:
        filename (str): name of the file to write
        text (str): text to write to the file
    Returns:
        number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
