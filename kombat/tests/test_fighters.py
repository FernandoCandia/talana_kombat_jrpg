import pytest

from kombat.fighters import Fighter, Attack
from kombat.lib import constants


class TestFighter:
    fighter_name = constants.TonynStalloneFighter.NAME

    @pytest.fixture()
    def tonyn_stallone_attacks(self):
        return [
            Attack(name=constants.TaladokenAttack, damage=3, combination="DSD+P"),
            Attack(name=constants.RemuyukenAttack, damage=2, combination="SD+K"),
            Attack(name=constants.KickAttack, damage=1, combination="K"),
            Attack(name=constants.PunchAttack, damage=1, combination="P")
        ]

    def test_make_move_nothing(self):
        fighter = Fighter(name=self.fighter_name)
        message, damage = fighter.make_move("")

        assert message == f"{self.fighter_name} no hace nada."
        assert damage == 0

    def test_make_move_hit_only(self):
        kick_attack = Attack(name=constants.KickAttack, damage=1, combination="K")
        fighter = Fighter(name=self.fighter_name, attacks=[kick_attack])
        message, damage = fighter.make_move("+K")

        assert message == f"{self.fighter_name} da {kick_attack.name}."
        assert damage == 1

    def test_make_move_movement_and_hit(self):
        punch_attack = Attack(name=constants.PunchAttack, damage=1, combination="P")
        fighter = Fighter(name=self.fighter_name, attacks=[punch_attack])
        message, damage = fighter.make_move("SD+P")
        assert message == f"{self.fighter_name} se mueve y da {punch_attack.name}."
        assert damage == 1

    def test_make_move_combination(self):
        taladoken_attack = Attack(name=constants.TaladokenAttack, damage=3, combination="DSD+P")
        fighter = Fighter(name=self.fighter_name, attacks=[taladoken_attack])
        message, damage = fighter.make_move("DSD+P")
        assert message == f"{self.fighter_name} conecta un {taladoken_attack.name}."
        assert damage == 3
