from fastapi import APIRouter, Request

from utils.neo4j_driver import driver

router = APIRouter()


@router.get("/common_movies", response_description="Compare movies on Mongo and on Neo4j", response_model=int)
def find_common_movies(request: Request):
    # Requesting neo4j
    query = '''
            MATCH (movie:Movie) 
            RETURN movie.title
            '''

    with driver.session() as session:
        raw_movies_in_neo4j = session.run(query).data()

    movies_in_neo4j = []
    for movie in raw_movies_in_neo4j:
        movies_in_neo4j.append(movie['movie.title'])

    # requesting mongodb
    raw_movies_in_mongo = request.app.database["movies"].find({}, {'title': 1, '_id': 0})

    movies_in_mongo = []
    for movie in raw_movies_in_mongo:
        movies_in_mongo.append(movie['title'])

    common_count = res = len(set(movies_in_neo4j) & set(movies_in_mongo))

    return common_count
