from pydantic import BaseModel

from typing import Sequence


class LocationBase(BaseModel):
    name: str
    description: str


class LocationCreate(LocationBase):
    name: str
    description: str


class LocationUpdate(LocationBase):
    name: str


# Properties shared by models stored in DB
class LocationInDBBase(LocationBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Location(LocationInDBBase):
    pass


# Properties properties stored in DB
class LocationInDB(LocationInDBBase):
    pass


class LocationSearchResults(BaseModel):
    results: Sequence[Location]
