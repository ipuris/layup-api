from pydantic import BaseModel
from ulid import ULID

from app.domain.valueobjects import Name


class Basketballer(BaseModel):
    id: ULID
    nickname: str
    name: Name | None = None
    home_court_id: ULID | None = None
    shoes_ids: list[ULID] = []
    ball_ids: list[ULID] = []

