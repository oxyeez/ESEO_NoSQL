from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional, Union
from typing import List
from datetime import datetime

class Artist(BaseModel):
    id: str = Field(alias="_id")
    last_name: str = Field(...)
    first_name: str = Field(...)
    birth_date: Optional[str] = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "artist:209",
                "last_name": "Machet",
                "first_name": "Titouan",
                "birth_date": "09/01/2001"
            }
        }


class ArtistUpdate(BaseModel):
    last_name: Optional[str]
    first_name: Optional[str]
    birth_date: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "last_name": "Delétang",
                "first_name": "Jules",
                "birth_date": "07/04/2000"
            }
        }

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class Awards(BaseModel):
    win: Optional[int] = None
    nominations: Optional[int] = None
    text: Optional[str] = None

class IMDB(BaseModel):
    rating: Optional[float] = None
    votes: Optional[int] = None
    id: Optional[int] = None

class Viewer(BaseModel):
    rating: Union[float, int, None] = None
    numReviews: Optional[int] = None
    meter: Optional[int] = None

class Critic(BaseModel):
    meter: Optional[int] = None
    numReviews: Optional[int] = None
    rating: Union[int, float, None] = None

class Tomatoes(BaseModel):
    consensus: Optional[str] = None
    critic: Optional[Critic] = None
    dvd: Optional[datetime] = None
    fresh: Optional[int] = None
    lastUpdated: Optional[datetime] = None
    production: Optional[str] = None
    rotten: Optional[int] = None
    viewer: Optional[Viewer] = None
    website: Optional[str] = None


class Movie(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    #TODO maybe find a way to display the id
    awards: Optional[Awards] = None
    cast: Optional[List[str]] = None
    countries: Optional[List[str]] = None
    directors: Optional[List[str]] = None
    fullplot: Optional[str] = None
    genres: Optional[List[str]] = None
    imdb: Optional[IMDB] = None
    languages: Optional[List[str]] = None
    lastupdated: Optional[str] = None
    num_mflix_comments: Optional[int] = None
    plot: Optional[str] = None
    poster: Optional[str] = None
    rated: Optional[str] = None
    released: Optional[datetime] = None
    runtine: Optional[int] = None
    title: str = None
    tomatoes: Optional[Tomatoes] = None
    type: Optional[str] = Field(...)
    writers: Optional[List[str]] = None
    year: Optional[int] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "_id": "573a1391f29313caabcd8ce8",
                "awards": {
                    "win": 1,
                    "nominations": 2,
                    "text": "1 win."
                },
                "cast": [
                    "Buster Keaton",
                    "Tom McGuire",
                    "Ernest Torrence",
                    "Tom Lewis"
                ],
                "countries": [
                    "USA"
                ],
                "directors": [
                    "Charles Reisner",
                    "Buster Keaton"
                ],
                "fullplot": "Following through on a promise to his mother, William Canning Jr. goes to River Junction to meet his father who has not seen him since he was a child. The younger Canning isn't quite what the elder was expecting but the old man has bigger problems. He's being put out of business by J.J. King, who not only owns the local hotel and bank, but has recently introduced a new paddle wheel steamer that puts Cannings older boat, the Stonewall Jackson, to shame. Bill Jr. and Kitty King take a liking to each other much to the dismay of both of their fathers. When a fierce storm hits River Junction, Bill Jr. is forced to save Kitty, her father and his father.",
                "genres": [
                    "Action",
                    "Comedy",
                    "Drama"
                ],
                "imdb": {
                    "rating": 8,
                    "votes": 8617,
                    "id": 19421
                },
                "languages": [
                    "English"
                ],
                "lastupdated": "2015-09-07 01:03:31.287000000",
                "num_mflix_comments": 0,
                "plot": "The effete son of a cantankerous riverboat captain comes to join his father's crew.",
                "poster": "https://m.media-amazon.com/images/M/MV5BOTg2MjUyMjYyOV5BMl5BanBnXkFtZTgwNjM0NDAwMjE@._V1_SY1000_SX677_AL_.jpg",
                "rated": "NOT RATED",
                "released": "1928-05-20T00:00:00",
                "runtine": None,
                "title": "Steamboat Bill, Jr.",
                "tomatoes": {
                    "consensus": None,
                    "critic": {
                        "meter": 100,
                        "numReviews": 17,
                        "rating": 9
                    },
                    "dvd": "2001-11-20T00:00:00",
                    "fresh": 17,
                    "lastUpdated": "2015-09-15T17:02:42",
                    "production": "United Artists",
                    "rotten": 0,
                    "viewer": {
                        "rating": 4.1,
                        "numReviews": 5283,
                        "meter": 92
                    },
                    "website": None
                },
                "type": "movie",
                "writers": [
                    "Carl Harbaugh (story)"
                ],
                "year": 1928
            }
        }


class MovieUpdate(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    awards: Optional[Awards] = None
    cast: Optional[List[str]] = None
    countries: Optional[List[str]] = None
    directors: Optional[List[str]] = None
    fullplot: Optional[str] = None
    genres: Optional[List[str]] = None
    imdb: Optional[IMDB] = None
    languages: Optional[List[str]] = None
    lastupdated: Optional[str] = None
    num_mflix_comments: Optional[int] = None
    plot: Optional[str] = None
    poster: Optional[str] = None
    rated: Optional[str] = None
    released: Optional[datetime] = None
    runtine: Optional[int] = None
    title: Optional[str] = None
    tomatoes: Optional[Tomatoes] = None
    type: Optional[str] = Field(...)
    writers: Optional[List[str]] = None
    year: Optional[int] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "awards": {
                    "win": 1,
                    "nominations": 2,
                    "text": "1 win."
                },
                "cast": [
                    "Buster Keaton",
                    "Tom McGuire",
                    "Ernest Torrence",
                    "Tom Lewis"
                ],
                "countries": [
                    "USA"
                ],
                "directors": [
                    "Charles Reisner",
                    "Buster Keaton"
                ],
                "fullplot": "Following through on a promise to his mother, William Canning Jr. goes to River Junction to meet his father who has not seen him since he was a child. The younger Canning isn't quite what the elder was expecting but the old man has bigger problems. He's being put out of business by J.J. King, who not only owns the local hotel and bank, but has recently introduced a new paddle wheel steamer that puts Cannings older boat, the Stonewall Jackson, to shame. Bill Jr. and Kitty King take a liking to each other much to the dismay of both of their fathers. When a fierce storm hits River Junction, Bill Jr. is forced to save Kitty, her father and his father.",
                "genres": [
                    "Action",
                    "Comedy",
                    "Drama"
                ],
                "imdb": {
                    "rating": 8,
                    "votes": 8617,
                    "id": 19421
                },
                "languages": [
                    "English"
                ],
                "lastupdated": "2015-09-07 01:03:31.287000000",
                "num_mflix_comments": 0,
                "plot": "The effete son of a cantankerous riverboat captain comes to join his father's crew.",
                "poster": "https://m.media-amazon.com/images/M/MV5BOTg2MjUyMjYyOV5BMl5BanBnXkFtZTgwNjM0NDAwMjE@._V1_SY1000_SX677_AL_.jpg",
                "rated": "NOT RATED",
                "released": "1928-05-20T00:00:00",
                "runtine": None,
                "title": "Steamboat Bill, Jr.",
                "tomatoes": {
                    "consensus": None,
                    "critic": {
                        "meter": 100,
                        "numReviews": 17,
                        "rating": 9
                    },
                    "dvd": "2001-11-20T00:00:00",
                    "fresh": 17,
                    "lastUpdated": "2015-09-15T17:02:42",
                    "production": "United Artists",
                    "rotten": 0,
                    "viewer": {
                        "rating": 4.1,
                        "numReviews": 5283,
                        "meter": 92
                    },
                    "website": None
                },
                "type": "movie",
                "writers": [
                    "Carl Harbaugh (story)"
                ],
                "year": 1928
            }
        }

class Person(BaseModel):
    id: int = None
    name: str = None
    born: Optional[int] = None

class MovieBasic(BaseModel):
    id: int = None
    title: str = None
    tagline: str = None
    released: int = None
