from app.application.usecases import CreatePracticeUseCase
from app.domain.repositories import PracticeRepository

from .repositories import get_practice_repository


def get_create_practice_usecase(practice_repo: PracticeRepository = get_practice_repository()):
    return CreatePracticeUseCase(practice_repo=practice_repo)

