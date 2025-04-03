from ulid import ULID

from app.domain.entities.ShootingDrill import ShootingDrill


def test_field_goal_percentage():
    drill = ShootingDrill(id=ULID(), attempts=25, made=10)
    assert drill.field_goal_percentage == 40.0

