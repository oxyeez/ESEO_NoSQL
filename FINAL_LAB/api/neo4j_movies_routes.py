from fastapi import APIRouter
from typing import List, Dict, Union

from utils.neo4j_driver import driver
from models import Person, MovieBasic

router = APIRouter()


@router.get("/assessors/{movie}", response_description="List users who rated a movie", response_model=List[Person])
def find_assessors(movie: str):
    query = '''
            MATCH (assessor:Person)-[:REVIEWED]->(m:Movie) 
            WHERE m.title = $movie 
            RETURN assessor
            '''

    with driver.session() as session:
        assessors_in_db = session.run(query, movie=movie).data()

    assessors = []
    for assessor in assessors_in_db:
        p = Person(**assessor['assessor'])
        p.id = assessor['assessor'].id
        assessors.append(p)

    return assessors


@router.get("/assessor/{user}", response_description="List users who rated a movie",
            response_model=Dict[str, Union[int, List[MovieBasic]]])
def find_assessors(user: str):
    query = '''
            MATCH (p:Person)-[:REVIEWED]->(m:Movie) 
            WHERE p.name = $user 
            RETURN count(m) AS count, collect(m) AS movies
            '''

    with driver.session() as session:
        assessor_in_db = session.run(query, user=user).data()[0]
    print(assessor_in_db['movies'])
    assessor = {'count': assessor_in_db['count'], 'movies': []}

    for movie in assessor_in_db['movies']:
        print(movie)
        m = MovieBasic(**movie)
        m.id = movie.id
        assessor['movies'].append(m)

    return assessor
