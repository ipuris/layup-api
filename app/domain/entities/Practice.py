from pydantic import BaseModel, AwareDatetime
from ulid import ULID

from app.domain.entities.Drill import Drill


class Practice(BaseModel):
    id: ULID = ULID()
    participant_ids: list[ULID]
    drills: list[Drill] = []
    court_id: ULID | None = None
    started_at: AwareDatetime | None = None
    finished_at: AwareDatetime | None = None
