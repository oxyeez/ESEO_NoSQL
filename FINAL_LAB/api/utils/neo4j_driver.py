import json

from neo4j import GraphDatabase

with open('../config.json', 'r') as outfile:
    config = json.load(outfile)

neo4j_conf = config['NEO4J']
URI = neo4j_conf['URI']
USERNAME = neo4j_conf['USERNAME']
PASSWORD = neo4j_conf['PASSWORD']

driver = GraphDatabase.driver(uri=URI, auth=(USERNAME, PASSWORD), encrypted=False)
