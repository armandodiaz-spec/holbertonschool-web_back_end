#!/usr/bin/env python3
""" update topics"""
def update_topics(mongo_collection, name, topics):
    """topic update"""
    mongo_collection.update_many(
            { "name": name },
            { "$set": { "topics": topics } }
            )
