from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import Artist, ArtistUpdate

router = APIRouter()


@router.get("/", response_description="List all artists", response_model=List[Artist])
def list_artists(request: Request):
    return list(request.app.database["artists"].find(limit=100))


@router.get("/artist/{id}", response_description="Get a single artist", response_model=Artist)
def find_artist(id: str, request: Request):
    if (artist := request.app.database["artists"].find_one({"_id": id})) is not None:
        return artist
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist with id {id} not found")


@router.get("/filter", response_description="Filter artists", response_model=List[Artist])
def find_with_filter(request: Request, first_name: str = "", last_name: str = "", birth_date: str = ""):
    return list(request.app.database["artists"].find({"first_name": {"$regex":first_name},
                                                      "last_name": {"$regex":last_name},
                                                      "birth_date": {"$regex":birth_date}}))


@router.delete("/{id}", response_description="Delete an artist")
def delete_artist(id: str, request: Request, response: Response):
    delete_result = request.app.database["artists"].delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist with id {id} not found")


@router.post("/", response_description="Create a new artist", status_code=status.HTTP_201_CREATED, response_model=Artist)
def create_artist(request: Request, artist: Artist = Body(...)):
    artist = jsonable_encoder(artist)
    new_artist = request.app.database["artists"].insert_one(artist)
    created_artist = request.app.database["artists"].find_one({
        "_id": new_artist.inserted_id
    })
    return created_artist


@router.put("/{id}", response_description="Update an artist", response_model=Artist)
def update_artist(id: str, request: Request, artist: ArtistUpdate = Body(...)):
    artist = {k: v for k, v in artist.dict().items() if v is not None}
    if len(artist) >= 1:
        update_result = request.app.database["artists"].update_one(
            {"_id": id}, {"$set": artist}
        )
        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist with id {id} not found")
    if (existing_artist := request.app.database["artists"].find_one({"_id": id})) is not None:
        return existing_artist
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist with id {id} not found")
