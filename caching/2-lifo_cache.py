#!/usr/bin/python3
'''LIFOCache Module'''

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    inherits from BaseCaching and is a Last-In, First-Out caching system.
    """

    def put(self, key, item):
        """ Add an item in the cache,
        if the number of items is greater than the cache limit ('MAX_ITEMS=4'),
        last item in cache gets discarded

        :param key: The key for the cache entry.
        :param item: The value associated with the key.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data)[-1]
            print(f'DISCARD: {last_key}')
            del self.cache_data[last_key]

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        :param key: the key to be retrieved in the cache
        :returns: The value associated to the key, None otherwise
        """
        if key not in self.cache_data or key is None:
            return None

        return self.cache_data.get(key)
