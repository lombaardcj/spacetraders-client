from logger import logger
from pydantic import BaseModel
from typing import List

# this is a json representation of the system class
# {
#     "system": {
#         "symbol": "X1-DF55",
#         "sectorSymbol": "X1",
#         "type": "RED_STAR",
#         "x": 47,
#         "y": 38,
#         "waypoints": [
#             {
#                 "symbol": "X1-DF55-20250Z",
#                 "type": "PLANET",
#                 "x": -5,
#                 "y": 9
#             },
#             {
#                 "symbol": "X1-DF55-89861D",
#                 "type": "MOON",
#                 "x": -5,
#                 "y": 9
#             },
#             {
#                 "symbol": "X1-DF55-64862A",
#                 "type": "MOON",
#                 "x": -5,
#                 "y": 9
#             },
#             {
#                 "symbol": "X1-DF55-71593D",
#                 "type": "MOON",
#                 "x": -5,
#                 "y": 9
#             },
#             {
#                 "symbol": "X1-DF55-52054E",
#                 "type": "PLANET",
#                 "x": -1,
#                 "y": 5
#             },
#             {
#                 "symbol": "X1-DF55-17335A",
#                 "type": "ASTEROID_FIELD",
#                 "x": 30,
#                 "y": -5
#             },
#             {
#                 "symbol": "X1-DF55-32376B",
#                 "type": "GAS_GIANT",
#                 "x": 32,
#                 "y": -38
#             },
#             {
#                 "symbol": "X1-DF55-69207D",
#                 "type": "ORBITAL_STATION",
#                 "x": 32,
#                 "y": -38
#             },
#             {
#                 "symbol": "X1-DF55-49148D",
#                 "type": "PLANET",
#                 "x": 49,
#                 "y": -50
#             },
#             {
#                 "symbol": "X1-DF55-24439B",
#                 "type": "JUMP_GATE",
#                 "x": 57,
#                 "y": -57
#             }
#         ],
#         "factions": []
#     }
# }

class SystemWaypoint(BaseModel):
    symbol: str
    type: str
    x: int
    y: int

class System(BaseModel):
    symbol: str
    sectorSymbol: str
    type: str
    x: int
    y: int
    waypoints: List[SystemWaypoint]
    factions: List[str]

    @staticmethod
    def url_list():
        return f"systems"

    @staticmethod
    def url_get(symbol):
        logger.info(f"{System.url_list()}/{symbol}")
        return f"{System.url_list()}/{symbol}"
