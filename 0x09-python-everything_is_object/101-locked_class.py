#!/usr/bin/python3
"""Locked class"""


class LockedClass:
    """
    Stop user from instantiating new LockedClass attributes
    except attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
