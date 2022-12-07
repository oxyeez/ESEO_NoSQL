from fastapi import FastAPI
from pymongo import MongoClient
from routes import router as artist_router
import json

with open('../config/config.json', 'r') as outfile:
    config = json.load(outfile)

DATABASE_NAME = config['DATABASE_NAME']
COLLECTION_NAME = config['COLLECTION_NAME']
MONGODB_PORT = config['MONGODB_PORT']

app = FastAPI()


@app.on_event("startup")
def startup_cb_client():
    app.mongodb_client = MongoClient("mongodb://localhost:{}".format(MONGODB_PORT))
    app.database = app.mongodb_client[DATABASE_NAME]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(artist_router, tags=['artists'], prefix="/artists")
