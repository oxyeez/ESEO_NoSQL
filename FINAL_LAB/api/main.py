from fastapi import FastAPI
from pymongo import MongoClient
from neo4j import GraphDatabase

from FINAL_LAB.api.Configurator import Configurator
from artists_routes import router as artists_router
from movies_routes import router as movies_router

CONFIG_FILE_PATH = "../config.json"
configurator = Configurator(config_file_path=CONFIG_FILE_PATH)
config = configurator.final_config
db_type = config.db_type
print(f"Got the following config: {config}")

app = FastAPI()


@app.on_event("startup")
def startup_cb_client():
    if db_type == 'LOCAL':
        app.mongodb_client = MongoClient(f"mongodb://localhost:{config['DYN']['MONGODB_PORT']}")
    elif db_type == 'ATLAS':
        app.mongodb_client = MongoClient(f"mongodb+srv://{config['DYN']['ATLAS_USER']}:{config['DYN']['ATLAS_PASSWORD']}@{config['DYN']['ATLAS_CLUSTER_URL']}/{config['DYN']['MONGO_DATABASE_NAME']}?retryWrites=true&w=majority")

    app.database = app.mongodb_client[config['DYN']['MONGO_DATABASE_NAME']]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(artists_router, tags=['artists'], prefix="/artists")
app.include_router(movies_router, tags=['movies'], prefix="/movies")
