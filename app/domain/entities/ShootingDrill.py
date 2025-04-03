from app.domain.valueobjects.Hand import Hand

from .Drill import Drill


class ShootingDrill(Drill):
    hand: Hand | None = None
    attempts: int | None = None
    made: int | None = None

    @property
    def field_goal_percentage(self) -> float | None:
        if self.attempts is None or self.made is None:
            return None
        return (self.made / self.attempts) * 100.0

