import json
from pydantic import BaseModel, validator

from location import Location

class Agent(BaseModel):
    accountId: str
    credits: int
    headquarters: str
    symbol: str

    @validator("headquarters")
    def convert_headquarters(cls, v):
        return Location.from_string(v)

    @staticmethod
    def url_list():
        return "my/agent"
