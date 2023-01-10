from fastapi import FastAPI
from pymongo import MongoClient
from artists_routes import router as artists_router
from movies_routes import router as movies_router
import json

with open('../config.json', 'r') as outfile:
    config = json.load(outfile)

DB_TYPE = config['DB_TYPE']
if DB_TYPE == 'LOCAL':
    local_conf = config['LOCAL']
    DATABASE_NAME = local_conf['DATABASE_NAME']
    MONGODB_PORT = local_conf['MONGODB_PORT']
elif DB_TYPE == 'ATLAS':
    atlas_conf = config['ATLAS']
    USER = atlas_conf['USER']
    PASSWORD = atlas_conf['PASSWORD']
    CLUSTER_URL = atlas_conf['CLUSTER_URL']
    DATABASE_NAME = atlas_conf['DATABASE_NAME']

app = FastAPI()


@app.on_event("startup")
def startup_cb_client():
    if DB_TYPE == 'LOCAL':
        app.mongodb_client = MongoClient(f"mongodb://localhost:{MONGODB_PORT}")
    elif DB_TYPE == 'ATLAS':
        app.mongodb_client = MongoClient(f"mongodb+srv://{USER}:{PASSWORD}@{CLUSTER_URL}/{DATABASE_NAME}?retryWrites=true&w=majority")
    app.database = app.mongodb_client[DATABASE_NAME]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(artists_router, tags=['artists'], prefix="/artists")
app.include_router(movies_router, tags=['movies'], prefix="/movies")
