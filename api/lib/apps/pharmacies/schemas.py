from pydantic import BaseModel, Field

class Location(BaseModel):
    latitude: float = Field(ge=-90, le=90, description="Value must be in range -90 to 90")
    longitude: float = Field(ge=-180, le=180, description="Value must be in range -90 to 90")

class Pharmacy(BaseModel):
    name: str
    address: str
    city: str
    state: str
    zip_code: int
    distance: float
