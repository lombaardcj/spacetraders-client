#  { "meta": {
#     "total": 0,
#     "page": 0,
#     "limit": 0
#   }

from pydantic import BaseModel

class Meta(BaseModel):
    total: int
    page: int
    limit: int
