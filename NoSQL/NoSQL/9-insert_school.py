#!/usr/bin/env python3
"""indi de insert pythonda"""
def insert_school(mongo_collection, **kwargs):
    """document insert ele 
    kwargs key value pairleridi"""
    result = mongo_collection.insert_one(kwargs)
    """inserts a single doc"""
    return result.inserted_id
    """to return the id"""
