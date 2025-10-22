#!/usr/bin/env python3
"""List all documents"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """List all documents"""
    return mongo_collection.find()


def insert_school(mongo_collection, **kwargs):
    """Insert a document"""
    return mongo_collection.insert_one(kwargs).inserted_id


def schools_by_topic(mongo_collection, topic):
    """list schools by topic"""
    return mongo_collection.find({"topics": {"$elemMatch": {"$eq": topic}}})


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    school_collection = client.my_db.school

    j_schools = [
        {"name": "Holberton school", "topics": ["Algo", "C", "Python", "React"]},
        {"name": "UCSF", "topics": ["Algo", "MongoDB"]},
        {"name": "UCLA", "topics": ["C", "Python"]},
        {"name": "UCSD", "topics": ["Cassandra"]},
        {"name": "Stanford", "topics": ["C", "React", "Javascript"]},
    ]
    for j_school in j_schools:
        insert_school(school_collection, **j_school)

    schools = schools_by_topic(school_collection, "Python")
    for school in schools:
        print(
            "[{}] {} {}".format(
                school.get("_id"), school.get("name"), school.get("topics", "")
            )
        )
