from pydantic import BaseModel, Field
from typing import Optional
import uuid


class Artist(BaseModel):
    id: str = Field(alias="_id")
    last_name: str = Field(...)
    first_name: str = Field(...)
    birth_date: str = Field(...)
    hobbies: Optional[str]

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
