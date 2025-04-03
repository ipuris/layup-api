from pydantic import BaseModel
from ulid import ULID


class Ball(BaseModel):
    id: ULID
