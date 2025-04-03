from pydantic import BaseModel, AwareDatetime
from ulid import ULID


class CreatePracticeCommand(BaseModel):
    participant_ids: list[ULID]
    court_id: ULID | None = None
    started_at: AwareDatetime | None = None
    finished_at: AwareDatetime | None = None
