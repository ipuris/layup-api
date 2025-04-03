from abc import ABC, abstractmethod

from ulid import ULID

from app.domain.entities import Practice


class PracticeRepository(ABC):
    @abstractmethod
    async def get_by_id(self, practice_id: ULID) -> Practice:
        raise NotImplementedError

    @abstractmethod
    async def get_by_basketballer_id(self, basketballer_id: ULID) -> Practice:
        raise NotImplementedError

    @abstractmethod
    async def add(self, practice: Practice) -> Practice:
        raise NotImplementedError

    @abstractmethod
    async def save(self, practice: Practice) -> Practice:
        raise NotImplementedError
