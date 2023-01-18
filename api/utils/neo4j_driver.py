import json

from neo4j import GraphDatabase
from .Configurator import configurator

config = configurator.final_config['NEO4J']
driver = GraphDatabase.driver(uri=config['URI'], auth=(config['USERNAME'], config['PASSWORD']), encrypted=False)
