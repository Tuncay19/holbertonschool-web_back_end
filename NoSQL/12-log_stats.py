#!/usr/bin/env python3
"""
Module to provide stats about Nginx logs in MongoDB
"""
from pymongo import MongoClient


def log_stats():
    """
    Displays stats about Nginx logs: total count, methods count,
    and specific GET /status count.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    total = nginx_collection.count_documents({})
    print("{} logs".format(total))

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_check))


if __name__ == "__main__":
    log_stats()
