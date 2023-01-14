from fastapi import FastAPI
from pymongo import MongoClient

from mongo_artists_routes import router as mongo_artists_router
from mongo_movies_routes import router as mongo_movies_router
from neo4j_movies_routes import router as neo4j_movies_router

import json

with open('../config.json', 'r') as outfile:
    config = json.load(outfile)

DB_TYPE = config['DB_TYPE']
if DB_TYPE == 'LOCAL':
    local_conf = config['LOCAL']
    MONGODB_DATABASE_NAME = local_conf['DATABASE_NAME']
    MONGODB_PORT = local_conf['MONGODB_PORT']
elif DB_TYPE == 'ATLAS':
    atlas_conf = config['ATLAS']
    ATLAS_USER = atlas_conf['USER']
    ATLAS_PASSWORD = atlas_conf['PASSWORD']
    ATLAS_CLUSTER_URL = atlas_conf['CLUSTER_URL']
    MONGODB_DATABASE_NAME = atlas_conf['DATABASE_NAME']


app = FastAPI()


@app.on_event("startup")
def startup_cb_client():
    if DB_TYPE == 'LOCAL':
        app.mongodb_client = MongoClient(f"mongodb://localhost:{MONGODB_PORT}")
    elif DB_TYPE == 'ATLAS':
        app.mongodb_client = MongoClient(f"mongodb+srv://{ATLAS_USER}:{ATLAS_PASSWORD}@{ATLAS_CLUSTER_URL}/{MONGODB_DATABASE_NAME}?retryWrites=true&w=majority")
    app.database = app.mongodb_client[MONGODB_DATABASE_NAME]




@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(mongo_artists_router, tags=['artists from mongodb'], prefix="/mongo_artists")
app.include_router(mongo_movies_router, tags=['movies from mongodb'], prefix="/mongo_movies")
app.include_router(neo4j_movies_router, tags=['movies from neo4j'], prefix="/neo4j_movies")
