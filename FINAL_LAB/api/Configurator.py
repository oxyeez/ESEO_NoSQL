import json


class Configurator:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.config = self.extract_config()
        self.db_type = self.config['DB_TYPE']
        self.final_config = {
            "NEO4J": {},
            "DYN": {}
        }
        self.make_config()

    def extract_config(self):
        with open(self.config_file_path, "r") as outfile:
            return json.load(outfile)

    def make_config(self):
        # build NEO4J config
        self.final_config['NEO4J'] = {
            "NEO4J_URI": self.config['NEO4J']['NEO4J_URI'],
            "NEO4J_USERNAME": self.config['NEO4J']['NEO4J_USERNAME'],
            "NEO4J_PASSWORD": self.config['NEO4J']['NEO4J_PASSWORD']
        }

        # build dynamic config
        if self.db_type == "LOCAL":
            self.final_config['DYN'] = {
                "MONGO_DATABASE_NAME": self.config['LOCAL']['DATABASE_NAME'],
                "MONGODB_PORT": self.config['LOCAL']['MONGODB_PORT']
            }
        elif self.db_type == "ATLAS":
            self.final_config['DYN'] = {
                "ATLAS_USER": self.config['ATLAS']['USER'],
                "ATLAS_PASSWORD": self.config['ATLAS']['PASSWORD'],
                "ATLAS_CLUSTER_URL": self.config['ATLAS']['CLUSTER_URL'],
                "MONGO_DATABASE_NAME": self.config['ATLAS']['DATABASE_NAME']
            }
        else:
            print("Unknown DB_TYPE...")