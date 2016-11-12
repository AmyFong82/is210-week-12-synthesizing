#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A simple custom exception class."""


class BaseError(Exception):
    """An extension of Exception class."""
    pass


class StringError(BaseError, TypeError):
    """A subclass to BaseError and TypeError."""
    pass


class NumberError(BaseError, TypeError):
    """A subclass to BaseError and TypeError."""
    pass


class NonZeroError(NumberError):
    """A subclass to NumberError."""
    pass
