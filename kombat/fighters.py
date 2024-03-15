from collections import namedtuple


Attack = namedtuple(typename='Attack', field_names=['name', 'damage', 'combination'])


class Fighter:
    def __init__(self, name: str, energy_points: int = 6, attacks: list[Attack] = None):
        self.name = name
        self.energy_points = energy_points
        self.attacks = attacks if attacks is not None else []

    def make_move(self, player_turn) -> tuple[str, int]:
        if not player_turn:
            return f"{self.name} no hace nada.", 0

        movement, hit = player_turn.split("+")

        for attack in self.attacks:
            if len(attack.combination) > 1 and attack.combination in player_turn:
                return f"{self.name} conecta un {attack.name}.", attack.damage
            elif movement and attack.combination == hit:
                return f"{self.name} se mueve y da {attack.name}.", attack.damage
            elif not movement and attack.combination == hit:
                return f"{self.name} da {attack.name}.", attack.damage
            elif movement and not hit:
                return f"{self.name} se mueve.", 0
