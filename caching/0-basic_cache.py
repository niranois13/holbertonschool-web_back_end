#!/usr/bin/python3
'''Module  '''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Class BasicCache that inherits from BaseCaching and is a caching system.
    """

    def put(self, key, item):
        """ Add an item in the cache
        :param key: The key for the cache entry.
        :param item: The value associated with the key.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        :param key: the key to be retrieved in the cache
        :returns: The value associated to the key, None otherwise
        """
        if key not in self.cache_data or key is None:
            return None

        return self.cache_data[key]
