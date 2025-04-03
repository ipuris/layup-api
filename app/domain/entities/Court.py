from pydantic import BaseModel
from ulid import ULID

from app.domain.valueobjects import GeoLocation


class Court(BaseModel):
    id: ULID
    name: str
    location: GeoLocation | None = None

