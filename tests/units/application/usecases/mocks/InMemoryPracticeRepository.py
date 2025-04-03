from ulid import ULID

from app.domain.entities import Practice
from app.domain.repositories import PracticeRepository


class InMemoryPracticeRepository(PracticeRepository):
    def __init__(self):
        self.store: dict[str, Practice] = {}

    async def get_by_id(self, practice_id: ULID) -> Practice:
        return self.store.get(str(practice_id))

    async def get_by_basketballer_id(self, basketballer_id: ULID) -> Practice:
        return self.store[str(basketballer_id)]

    async def add(self, practice: Practice) -> Practice:
        self.store[str(practice.id)] = practice
        return practice

    async def save(self, practice: Practice) -> Practice:
        self.store[str(practice.id)] = practice
        return practice

