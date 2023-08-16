#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if object an inherited instance of a class.

    Args:
        obj (any): object to check.
        a_class (type): class to match the type of obj to.
    Returns:
        If obj is inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
