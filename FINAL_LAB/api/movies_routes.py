from fastapi import APIRouter, Request, HTTPException, status
from typing import List

from models import Movie

router = APIRouter()


@router.get("/", response_description="List all movies", response_model=List[Movie])
def list_movies(request: Request):
    return list(request.app.database["movies"].find(limit=100))


@router.get("/filter", response_description="Filter movies", response_model=List[Movie])
def find_with_filter(request: Request, title: str = "", actors: str = ""):
    if actors != "":
        return list(request.app.database["movies"].find({"title": {"$regex":title},
                                                        "cast": {"$all": actors.split(',')}}))
    else:
        return list(request.app.database["movies"].find({"title": {"$regex": title}}))
