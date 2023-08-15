#!/usr/bin/python3

"""Defines a writing function."""

def write_file(filename="", text=""):
    """Write a string to UTF8 text file.

    Args:
        filename (str): name of the file to write.
        text (str): text to write to the file.
    Returns:
        The nbr characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
