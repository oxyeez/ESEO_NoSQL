from fastapi import FastAPI
from pymongo import MongoClient
from neo4j import GraphDatabase
from artists_routes import router as artists_router
from movies_routes import router as movies_router
import json

with open('../config.json', 'r') as outfile:
    config = json.load(outfile)

DB_TYPE = config['DB_TYPE']
if DB_TYPE == 'LOCAL':
    local_conf = config['LOCAL']
    MONGO_DATABASE_NAME = local_conf['DATABASE_NAME']
    MONGODB_PORT = local_conf['MONGODB_PORT']
elif DB_TYPE == 'ATLAS':
    atlas_conf = config['ATLAS']
    ATLAS_USER = atlas_conf['USER']
    ATLAS_PASSWORD = atlas_conf['PASSWORD']
    ATLAS_CLUSTER_URL = atlas_conf['CLUSTER_URL']
    MONGO_DATABASE_NAME = atlas_conf['DATABASE_NAME']

neo4j_conf = config['NEO4J']
NEO4J_URI = neo4j_conf['URI']
NEO4J_USERNAME = neo4j_conf['USERNAME']
NEO4J_PASSWORD = neo4j_conf['NEO4J_PASSWORD']
NEO4J_DATABASE_NAME = neo4j_conf['DATABASE_NAME']

app = FastAPI()


@app.on_event("startup")
def startup_cb_client():
    if DB_TYPE == 'LOCAL':
        app.mongodb_client = MongoClient(f"mongodb://localhost:{MONGODB_PORT}")
    elif DB_TYPE == 'ATLAS':
        app.mongodb_client = MongoClient(f"mongodb+srv://{ATLAS_USER}:{ATLAS_PASSWORD}@{ATLAS_CLUSTER_URL}/{MONGO_DATABASE_NAME}?retryWrites=true&w=majority")

    app.database = app.mongodb_client[MONGO_DATABASE_NAME]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(artists_router, tags=['artists'], prefix="/artists")
app.include_router(movies_router, tags=['movies'], prefix="/movies")
