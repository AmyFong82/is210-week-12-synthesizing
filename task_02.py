#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A custom error subclassed by Exception."""


class CustomError(Exception):
    """A custom error, subclassed to Exception."""

    def __init__(self, msg, cause):
        """Constructor for CustomError.

        Args:
            msg (str): A message.
            cause (str): Cause of the error.

        Attributes:
            cause (str): Cause of the error.
        """
        Exception.__init__(self, msg)
        self.cause = cause
