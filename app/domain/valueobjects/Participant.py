from pydantic import BaseModel
from ulid import ULID


class Participant(BaseModel):
    basketballer_id: ULID
    shoes_id: ULID
    ball_ids: list[ULID]
