#!/usr/bin/env python3
""" nginx logs statistics """
from pymongo import MongoClient

def count(coll, method):
    """ gormursen documenti count da """
    res = coll.count_documents({"method": method})
    return res

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    print(f"{nginx_collection.count_documents({})} logs")
    print("Methods:")
    for i in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(f"	method {i}: {count(nginx_collection, i)}")
    print("{} status check".format(nginx_collection.count_documents({"path": "/status"})))
