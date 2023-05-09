from pydantic import BaseModel

class Location(BaseModel):
    sector: str   #X1
    system: str   #X1-DF55
    waypoint: str #X1-DF55-20250Z

    @classmethod
    def from_string(cls, location_str):
        parts = location_str.split('-')
        if len(parts) != 3:
            raise ValueError(f"invalid location string: {location_str}")
        return cls(sector=parts[0], system=f"{parts[0]}-{parts[1]}", waypoint=f"{parts[0]}-{parts[1]}-{parts[2]}")
