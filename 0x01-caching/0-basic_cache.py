#!/usr/bin/env python3
"""this dox contains func to define class"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """this class for catching info in key-value pairs
    methods:
        put: store a key-value pair
        get: retrieve the value associated with a key
    """
    def __init__(self):
        """func to initialize the class using init"""
        BaseCaching.__init__(self)

    def put(self, key, item):
        """func to store key value pair"""
        if key is None or item is None:
            pass

        else:
            self.cache_data[key] = item

    def get(self, key):
        """func to return value linked to key"""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]

        return None
