#!/usr/bin/env python3
"""this docs conatin BaseCaching module"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """this class contains FIFOCache defines caching system"""
    def __init__(self):
        """func to initialize class with parent"""
        super().__init__()

        self.usg = []

    def put(self, key, item):
        """func to catch key-value pair"""
        if key is None or item is None:
            pass

        else:
            le = len(self.cache_data)

            if le >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.usg[-1]))

                del self.cache_data[self.usg[-1]]
                del self.usg[-1]

            if key in self.usg:
                del self.usg[self.usg.index(key)]

            self.usg.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """func to return value linked to a given key or none"""
        if key is not None and key in self.cache_data.keys():
            del self.usg[self.usg.index(key)]
            self.usg.append(key)

            return self.cache_data[key]
        return None
