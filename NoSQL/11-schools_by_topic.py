#!/usr/bin/env python3
""" Module compiled with Python3 """


def schools_by_topic(mongo_collection, topic):
    """
    Function that returns the list of school having a specific topic.
    :param mongo_collection: the pymongo collection
    :param topic: str - the topic searched in the 'mogo_collection'
    """
    return [item for item in mongo_collection.find({"topics": topic})]
