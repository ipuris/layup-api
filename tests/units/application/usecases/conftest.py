import pytest

from .mocks import InMemoryPracticeRepository


@pytest.fixture(scope="function")
def practice_repository() -> InMemoryPracticeRepository:
    return InMemoryPracticeRepository()
