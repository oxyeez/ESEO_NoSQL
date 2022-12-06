from flask import Flask, request, json, Response
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

app = Flask(__name__)
