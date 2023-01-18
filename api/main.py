from fastapi import FastAPI
from pymongo import MongoClient

from mongo_artists_routes import router as mongo_artists_router
from mongo_movies_routes import router as mongo_movies_router
from neo4j_movies_routes import router as neo4j_movies_router
from mongo_neo4j_routes import router as mongo_neo4j_router

from utils.Configurator import configurator

config = configurator.final_config
db_type = configurator.db_type

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


app.include_router(mongo_artists_router, tags=['artists from mongodb'], prefix="/mongo_artists")
app.include_router(mongo_movies_router, tags=['movies from mongodb'], prefix="/mongo_movies")
app.include_router(neo4j_movies_router, tags=['movies from neo4j'], prefix="/neo4j_movies")
app.include_router(mongo_neo4j_router, tags=['movies from mongodb and neo4j'], prefix="/mongo_neo4j_movies")
