#!/usr/bin/env python3
"""this docs contains BaseCaching module"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """this class contain funcs to define FIFO caching system"""
    def __init__(self):
        """func to initialize class with parent's init method"""
        super().__init__()

        self.usg = []

    def put(self, key, item):
        """func to catch key-value"""
        if key is None or item is None:
            pass

        else:
            le = len(self.cache_data)

            if le >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.usg[0]))

                del self.cache_data[self.usg[0]]
                del self.usg[0]

            if key in self.usg:
                del self.usg[self.usg.index(key)]

            self.usg.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """func to return value linked to given key orNone"""
        if key is not None and key in self.cache_data.keys():
            del self.usg[self.usg.index(key)]

            self.usg.append(key)
            return self.cache_data[key]

        return None
