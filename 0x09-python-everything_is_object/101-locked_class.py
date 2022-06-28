#!/usr/bin/python3
"""
create a locked class
"""


class LockedClass:
    """
    locked class - prevents the user from dynamically creating
    new instance attributes, except if the new instance
    attribute is explictly in the __slots__
    """
    __slots__ = ['first_name']
