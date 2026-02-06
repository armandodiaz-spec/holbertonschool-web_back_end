#!/usr/bin/env python3
"""returns list of school"""
def schools_by_topic(mongo_collection, topic):
    """search topic"""
    return list(mongo_collection.find({ "topics": topic }))
