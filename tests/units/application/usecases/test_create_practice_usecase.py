import pytest
from ulid import ULID

from app.application.commands import CreatePracticeCommand
from app.application.usecases import CreatePracticeUseCase


@pytest.mark.asyncio
async def test_create_practice_usecase(practice_repository):
    create_practice_usecase = CreatePracticeUseCase(practice_repo=practice_repository)

    participant_ids = [ULID(), ULID()]
    court_id = ULID()

    command = CreatePracticeCommand(
        participant_ids=participant_ids,
        court_id=court_id,
    )

    practice = await create_practice_usecase(command)

    assert practice.participant_ids == participant_ids
    assert practice.court_id == court_id

    stored_practice = await practice_repository.get_by_id(practice.id)
    assert stored_practice is not None
    assert stored_practice.id == practice.id

