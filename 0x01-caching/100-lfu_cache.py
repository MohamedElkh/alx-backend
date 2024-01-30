#!/usr/bin/env python3
"""this docs contains BaseCaching module"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """this class contains FIFOCache to defines a FIFO"""
    def __init__(self):
        """func to initialize class with parent"""
        super().__init__()

        self.usg = []
        self.freq = {}

    def put(self, key, item):
        """func to cache key-value pair"""
        if key is None or item is None:
            pass

        else:
            le = len(self.cache_data)

            if le >= BaseCaching.MAX_ITEMS and key not in self.cache_data:

                fu = min(self.freq.values())
                fu_ks = []

                for ky, val in self.freq.items():
                    if val == fu:
                        fu_ks.append(ky)

                if len(fu_ks) > 1:
                    fu_r = {}

                    for ky in fu_ks:
                        fu_r[ky] = self.usg.index(ky)

                    disc = min(fu_r.values())
                    disc = self.usg[disc]

                else:
                    disc = fu_ks[0]

                print("DISCARD: {}".format(disc))

                del self.cache_data[disc]
                del self.usg[self.usg.index(disc)]

                del self.freq[disc]

            if key in self.freq:
                self.freq[key] += 1
            else:
                self.freq[key] = 1

            if key in self.usg:
                del self.usg[self.usg.index(key)]

            self.usg.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """func to return value linked to a given key"""
        if key is not None and key in self.cache_data.keys():
            del self.usg[self.usg.index(key)]

            self.usg.append(key)
            self.freq[key] += 1

            return self.cache_data[key]
        return None
