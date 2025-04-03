from pydantic import BaseModel
from ulid import ULID


class Drill(BaseModel):
    id: ULID

