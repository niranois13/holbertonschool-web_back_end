#!/usr/bin/env python3
"""Module compiled with Python3"""


def list_all(mongo_collection):
    """
    Function that lists all documents in a mongoDB collection
    """
    list = []
    for document in mongo_collection.find():
        list.append(document)
    return list
