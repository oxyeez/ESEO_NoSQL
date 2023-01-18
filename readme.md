# No-SQL Class - ESEO

This project aims to provide an API (FastAPI Python) in the way to deal with a MongoDB NoSQL database.

To run this project locally:

- Create a json configuration file at the root of the project as the following pattern:
```json
{
  "DB_TYPE": "ATLAS", //the type of system to use for mongodb, choices : ATLAS, LOCAL
  "LOCAL": {
    "DATABASE_NAME": <database_name>,
    "MONGODB_PORT": <mongodb_port>
  },
  "ATLAS": {
    "USER": <db_access_user>,
    "PASSWORD": <db_access_password>,
    "CLUSTER_URL": <atlas_cluster_url>,
    "DATABASE_NAME": <database_name>
  },
  "NEO4J": {
    "URI": <neo4j_db_uri>,
    "USERNAME": <neo4j_access_username>,
    "PASSWORD": <neo4j_access_password> // bolt://<ip>:<port>
  }
}
```

- After that, you can run the app by typing the following command in your terminal:
```bash
$ pip install -r requirement.txt
$ cd ./api
$ python -m uvicorn main:app --reload
```

- Once the app is launched, you can visit the page: http://localhost:8000/docs and exploit the CRUD features
