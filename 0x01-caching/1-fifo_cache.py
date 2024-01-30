#!/usr/bin/env python3
"""this docs contains BaseCaching module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """this class FIFOCache defines a FIFO caching system"""
    def __init__(self):
        """func to init the class with parent"""
        super().__init__()

        self.ordx = []

    def put(self, key, item):
        """func to catch key-value pair"""
        if key is None or item is None:
            pass

        else:
            le = len(self.cache_data)

            if le >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.ordx[0]))

                del self.cache_data[self.ordx[0]]
                del self.ordx[0]

            self.ordx.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """func to return value linked to a given key"""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]

        return None
