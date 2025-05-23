#!/usr/bin/python3
'''LFUCache Module'''

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    inherits from BaseCaching and is a Least Frequently Used caching system
    """

    def __init__(self):
        """ Initiliazes an used_order variable
        to keep track of the cache's key usage.
        """
        super().__init__()
        self.used_order = []
        self.used_count = {}

    def put(self, key, item):
        """Add an item in the cache,
        if the number of items is greater than the cache limit ('MAX_ITEMS=4'),
        the least frenquently used item in cache gets discarded.
        If many keys have the same count of uses,
        the least recently used item in cache gets discarded.

        :param key: The key for the cache entry.
        :param item: The value associated with the key.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.used_count[key] += 1
            self.used_order.remove(key)
            self.used_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_count = min(self.used_count.values())
                total_unused_keys = [k for k in self.used_order if self.used_count[k] == min_count]
                unused_key = total_unused_keys[0]
                del self.cache_data[unused_key]
                self.used_order.remove(unused_key)
                del self.used_count[unused_key]
                print(f'DISCARD: {unused_key}')

        self.cache_data[key] = item
        self.used_count[key] = 1
        self.used_order.append(key)

    def get(self, key):
        """ Get an item by key,
        the key is append to the used_order list
        to keep track of the cache key usage,
        used_count of this key is update by 1

        :param key: the key to be retrieved in the cache
        :returns: The value associated to the key, None otherwise
        """
        if key not in self.cache_data or key is None:
            return None

        self.used_count[key] += 1
        self.used_order.remove(key)
        self.used_order.append(key)

        return self.cache_data.get(key)
