# No-SQL Class - ESEO

This project aims to provide an API (FastAPI Python) in the way to deal with a MongoDB NoSQL database.

To run this project locally:

- Create a json configuration file as the following pattern:
```json
{
  "DB_TYPE": "ATLAS", //the type of system to use, choices : ATLAS, LOCAL OR NEO4J
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
    "NEO4J_URI": <neo4j_db_uri>,
    "NEO4J_USERNAME": <neo4j_username>,
    "NEO4J_PASSWORD": <neo4j_password>
  }
}
```

- After that, you can run the app by typing the following command in your terminal:
```bash
$ cd ./api
$ python -m uvicorn main:app --reload
```

- Once the app is launched, you can visit the page: http://localhost:8000/docs and exploit the CRUD features
