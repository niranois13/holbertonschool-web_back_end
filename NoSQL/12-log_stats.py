#!/usr/bin/env python3
"""
Module compiled with Python3
Python script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017')
    db = client.logs
    collection = db.nginx

    print(f"{collection.count_documents({})} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("Methods:")

    for method in methods:
        m_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {m_count}")

    s_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{s_count} status check")
