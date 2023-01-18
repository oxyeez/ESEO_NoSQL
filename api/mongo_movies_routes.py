from fastapi import APIRouter, Request, Response, HTTPException, status, Body
from fastapi.encoders import jsonable_encoder
from typing import List

from models import Movie, MovieUpdate

router = APIRouter()


@router.get("/", response_description="List all movies", response_model=List[Movie])
def list_movies(request: Request):
    return list(request.app.database["movies"].find(limit=100))


@router.get("/filter", response_description="Filter movies", response_model=List[Movie])
def find_with_filter(request: Request, title: str = "", actor: str = ""):
    if title == '' or title is None:
        return list(request.app.database["movies"].find({"cast": {"$regex": actor}}))
    elif actor == '' or actor is None:
        return list(request.app.database["movies"].find({"title": {"$regex": title}}))
    else:
        return list(request.app.database["movies"].find({"title": {"$regex": title},
                                                         "cast": {"$regex": actor}}))


@router.post("/", response_description="Create a new movie", status_code=status.HTTP_201_CREATED, response_model=Movie)
def create_movie(request: Request, movie: Movie = Body(...)):
    movie = jsonable_encoder(movie)
    new_movie = request.app.database["movies"].insert_one(movie)
    if (created_movie := request.app.database["movies"].find_one({"_id": new_movie.inserted_id})) is not None:
        return created_movie
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie not created")


@router.put("/{title}", response_description="Update a movie", response_model=Movie)
def update_movie(title: str, request: Request, movie: MovieUpdate = Body(...)):
    movie = {k: v for k, v in movie.dict().items() if v is not None}
    if len(movie) >= 1:
        update_result = request.app.database["movies"].update_one(
            {"title": title}, {"$set": movie}
        )
        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with id {id} not found")
    if (existing_movie := request.app.database["movies"].find_one({"title": title})) is not None:
        return existing_movie
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with title {title} not found")
