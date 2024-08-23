#!/usr/bin/env python3
"""Module compiled with Python3"""


def insert_school(mongo_collection, **kwargs):
    """
    Function that inserts a new document in mongoDB collection based on kwargs
    :param mongo_collection: the pymongo collection
    :param **kwargs: dict - Additional keyword arguments.
        These arguments can be any number of key-value pairs, where the keys
        are strings representing the argument names, and the values are the
        corresponding values.
    Returns: the updated document
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
