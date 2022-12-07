from flask import Flask, request, json, Response
from pymongo import MongoClient, response
from fastapi import HTTPException, status
import os
import json

with open("./config.json", "r") as outfile:
    config = json.load(outfile)

DATABASE_NAME = config["DATABASE_NAME"]
COLLECTION_NAME = config["COLLECTION_NAME"]
MONGODB_PORT = config["MONGODB_PORT"]


class MongoAPI:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:{}/'.format(MONGODB_PORT))
        self.db = getattr(self.client, DATABASE_NAME)
        self.collection = getattr(self.db, COLLECTION_NAME)

    def get_artists(self):
        return self.collection.find(limit=1000)

    def get_artist(self, id_artist):
        if (artist := self.collection.find_one({ "_id": id_artist })) is not None:
            return artist
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist with id {id_artist} not found")

    def delete_artist(self, id_artist):
        delete_result = self.collection.delete_one({ "_id": id_artist })
        if delete_result.deleted_count == 1:
            response.status_code = status.HTTP_204_NO_CONTENT
            return response
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist with id {id_artist} not found")

api = MongoAPI()
