#!/usr/bin/env python3
""" Module compiled with Python3"""


def update_topics(mongo_collection, name, topics):
    """
    Function that changes field in document based on name field.
    :param mongo_collection: the pymongo collection
    :param name: str - the school name to update
    :param topics: list[str] - list of topics approached in the school
    """
    name_field = {"name": name}
    value_field = {"$set": {"topics": topics}}
    mongo_collection.update_many(name_field, value_field)
