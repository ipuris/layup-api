from pydantic import BaseModel
from ulid import ULID


class Shoes(BaseModel):
    id: ULID
