from fastapi import APIRouter
from typing import List, Dict, Union

from utils.neo4j_driver import driver
from models import Person, MovieBasic

router = APIRouter()


@router.get("/assessors/{movie}", response_description="List users who rated a movie", response_model=List[Person])
def find_assessors(movie: str):
    query = f"""
            MATCH (assessor:Person)-[:REVIEWED]->(m:Movie) 
            WHERE m.title CONTAINS '{movie}' 
            RETURN assessor
            """

    with driver.session() as session:
        assessors_in_db = session.run(query, movie=movie).data()

    assessors = []
    for assessor in assessors_in_db:
        p = Person(**assessor['assessor'])
        p.id = assessor['assessor'].id
        assessors.append(p)

    return assessors


@router.get("/assessments", response_description="List movies rated by all user or a requested user and give the count",
            response_model=List[Dict[str, Union[int, Person, List[MovieBasic]]]])
def find_assessments(user: str = None):
    if user is None or user == '':
        query = f"""
                MATCH (p:Person)-[:REVIEWED]->(m:Movie)
                RETURN p as assessor, count(m) AS count, collect(m) AS movies
                """

    else:
        query = f"""
                MATCH (p:Person)-[:REVIEWED]->(m:Movie) 
                WHERE p.name CONTAINS '{user}'
                RETURN p as assessor, count(m) AS count, collect(m) AS movies
                """

    with driver.session() as session:
        assessments_in_db = session.run(query).data()

    assessments = []
    for assessment_in_db in assessments_in_db:
        assessor = Person(**assessment_in_db['assessor'])
        assessor.id = assessment_in_db['assessor'].id

        movies = []
        for movie in assessment_in_db['movies']:
            m = MovieBasic(**movie)
            m.id = movie.id
            movies.append(m)

        assessments.append({'user': assessor, 'count': assessment_in_db['count'], 'movies': movies})

    return assessments
