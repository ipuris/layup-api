from pydantic import BaseModel
from pydantic_extra_types.coordinate import Latitude, Longitude


class GeoLocation(BaseModel):
    latitude: Latitude
    longitude: Longitude
