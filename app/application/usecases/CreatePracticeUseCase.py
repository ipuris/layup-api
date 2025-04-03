from app.application.commands import CreatePracticeCommand
from app.domain.entities import Practice
from app.domain.repositories import PracticeRepository


class CreatePracticeUseCase:
    def __init__(self, practice_repo: PracticeRepository):
        self.practice_repo = practice_repo

    async def __call__(self, command: CreatePracticeCommand) -> Practice:
        practice = Practice(
            participant_ids=command.participant_ids,
            court_id=command.court_id,
            started_at=command.started_at,
            finished_at=command.finished_at,
        )
        practice_added = await self.practice_repo.add(practice=practice)
        return practice_added

