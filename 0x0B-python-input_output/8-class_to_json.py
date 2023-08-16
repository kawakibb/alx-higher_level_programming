#!/usr/bin/python3
"""Defines Python classto-JSON function"""


def class_to_json(obj):
    """Return dictirepresntation of a simple data structure."""
    return obj.__dict__
