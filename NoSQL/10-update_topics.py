#!/usr/bin/env python3
"""update topics"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """List all documents"""
    return mongo_collection.find()


def update_topics(mongo_collection, name, topics):
    """Update topics"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    school_collection = client.my_db.school
    update_topics(
        school_collection, "Holberton school", ["Sys admin", "AI", "Algorithm"]
    )

    schools = list_all(school_collection)
    for school in schools:
        print(
            "[{}] {} {}".format(
                school.get("_id"), school.get("name"), school.get("topics", "")
            )
        )

    update_topics(school_collection, "Holberton school", ["iOS"])

    schools = list_all(school_collection)
    for school in schools:
        print(
            "[{}] {} {}".format(
                school.get("_id"), school.get("name"), school.get("topics", "")
            )
        )
