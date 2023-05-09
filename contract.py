from datetime import datetime
from typing import List
from pydantic import BaseModel

from meta import Meta

# a contract contains the following information provided in a json string

# {
#     "id": "clhg952sn017ws60drx1kl1e8",
#     "factionSymbol": "COSMIC",
#     "type": "PROCUREMENT",
#     "terms": {
#         "deadline": "2023-05-16T12:32:37.990Z",
#         "payment": {
#             "onAccepted": 135200,
#             "onFulfilled": 540800
#         },
#         "deliver": [
#             {
#                 "tradeSymbol": "ALUMINUM_ORE",
#                 "destinationSymbol": "X1-DF55-20250Z",
#                 "unitsRequired": 13000,
#                 "unitsFulfilled": 0
#             }
#         ]
#     },
#     "accepted": false,
#     "fulfilled": false,
#     "expiration": "2023-05-12T12:32:37.990Z"
# }

class Payment(BaseModel):
    onAccepted: int
    onFulfilled: int

class Deliver(BaseModel):
    tradeSymbol: str
    destinationSymbol: str
    unitsRequired: int
    unitsFulfilled: int

class Terms(BaseModel):
    deadline: datetime
    payment: Payment
    deliver: List[Deliver]

class Contract(BaseModel):
    id: str
    factionSymbol: str
    type: str
    terms: Terms
    accepted: bool
    fulfilled: bool
    expiration: datetime

    @staticmethod
    def url_list():
        return "my/contracts"

    def url_accept(self):
        return f"{self.url_list()}/{self.id}/accept"
