from fastapi import APIRouter, Request, Response, HTTPException, status, Body
from fastapi.encoders import jsonable_encoder
from typing import List

from models import Movie, MovieUpdate, ObjectId

router = APIRouter()


@router.get("/", response_description="List all movies", response_model=List[Movie])
def list_movies(request: Request):
    return list(request.app.database["movies"].find(limit=100))


@router.get("/movie/{id}", response_description="Get a single movie", response_model=Movie)
def find_artist(id: str, request: Request):
    if (movie := request.app.database["movies"].find_one({"_id": ObjectId(id)})) is not None:
        return movie
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with id {id} not found")


@router.get("/filter", response_description="Filter movies", response_model=List[Movie])
def find_with_filter(request: Request, title: str = "", actors: str = ""):
    if actors != "":
        return list(request.app.database["movies"].find({"title": {"$regex": title},
                                                         "cast": {"$all": actors.split(',')}}))
    else:
        return list(request.app.database["movies"].find({"title": {"$regex": title}}))


@router.delete("/{id}", response_description="Delete an movie")
def delete_movie(id: str, request: Request, response: Response):
    delete_result = request.app.database["movies"].delete_one({"_id": ObjectId(id)})
    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with id {id} not found")


@router.post("/", response_description="Create a new movie", status_code=status.HTTP_201_CREATED, response_model=Movie)
def create_movie(request: Request, movie: MovieUpdate = Body(...)):
    movie = jsonable_encoder(movie)
    new_movie = request.app.database["movies"].insert_one(movie)
    if (created_movie := request.app.database["movies"].find_one({"_id": new_movie.inserted_id})) is not None:
        return created_movie
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie not created")


@router.put("/{id}", response_description="Update a movie", response_model=Movie)
def update_movie(id: str, request: Request, movie: MovieUpdate = Body(...)):
    movie = {k: v for k, v in movie.dict().items() if v is not None}
    if len(movie) >= 1:
        update_result = request.app.database["movies"].update_one(
            {"_id": ObjectId(id)}, {"$set": movie}
        )
        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with id {id} not found")
    if (existing_movie := request.app.database["movies"].find_one({"_id": ObjectId(id)})) is not None:
        return existing_movie
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with id {id} not found")
