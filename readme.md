# No-SQL Class - ESEO

This project aims to provide an API (FastAPI Python) in the way to deal with a MongoDB NoSQL database.

To run this project locally:

- Create a json configuration file as the following pattern:
```json
{
  "DATABASE_NAME": <database_name>,
  "COLLECTION_NAME": <collection_name>,
  "MONGODB_PORT": <mongodb_port>
}
```

- After that, you can run the app by typing the following command in your terminal:
```bash
$ cd ./api
$ python -m uvicorn main:app --reload
```

- Once the app is launched, you can visit the page: http://localhost:8000/docs and exploit the CRUD features