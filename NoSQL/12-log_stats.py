#!/usr/bin/env python3
""" nginx logs statistics """
from pymongo import MongoClient


def count(coll, method):
    """ counts documents by HTTP method """
    return coll.count_documents({"method": method})


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx

    print(f"{nginx_collection.count_documents({})} logs")
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(f"\tmethod {method}: {count(nginx_collection, method)}")
    print("{} status check".format(
        nginx_collection.count_documents({"path": "/status"})))

