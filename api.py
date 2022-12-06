from flask import Flask, request, json, Response
from pymongo import MongoClient

app = Flask(__name__)


@app.route("/update")
