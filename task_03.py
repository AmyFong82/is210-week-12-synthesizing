#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


def exception_test(arg1, arg2, arg3):
    """A function that catch TypeError, KeyError and IndexError."""
    caught = False
    try:
        arg1[arg2].index(arg3)
    except (TypeError, LookupError):
        caught = True

    return caught
