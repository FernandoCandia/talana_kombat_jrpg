from kombat.fighters import Fighter, Attack
from kombat.lib import constants


def get_player_data_to_initialize_kombat(player_data: dict) -> (list, int, int, int):
    player_turns = []
    combinations_count = 0
    movements_count = 0
    hit_counts = 0
    for movements, hit in zip(player_data["movimientos"], player_data["golpes"]):
        movements_count += len(movements)
        hit_counts += len(hit)
        if movements and hit:
            combinations_count += 1
        player_turns.append(f"{movements}+{hit}" if movements or hit else "")

    return player_turns, combinations_count, movements_count, hit_counts


def get_players_turns_and_define_starting_player(kombat_data: dict) -> tuple[list, list, bool]:
    (
        tonyn_turns,
        tonyn_combinations_count,
        tonyn_movements_count,
        tonyn_hits_count,
    ) = get_player_data_to_initialize_kombat(player_data=kombat_data["player1"])
    (
        arnaldor_turns,
        arnaldor_combinations_count,
        arnaldor_movements_count,
        arnaldor_hits_count,
    ) = get_player_data_to_initialize_kombat(player_data=kombat_data["player2"])

    return (
        tonyn_turns,
        arnaldor_turns,
        (
            tonyn_combinations_count,
            tonyn_movements_count,
            tonyn_hits_count,
        )
        <= (
            arnaldor_combinations_count,
            arnaldor_movements_count,
            arnaldor_hits_count,
        ),
    )


def create_players(tonyn_starts: bool) -> tuple[Fighter, Fighter]:
    tonyn_stallone_attacks = [
        Attack(name=constants.TaladokenAttack.NAME, damage=3, combination="DSD+P"),
        Attack(name=constants.RemuyukenAttack.NAME, damage=2, combination="SD+K"),
        Attack(name=constants.PunchAttack.NAME, damage=1, combination="P"),
        Attack(name=constants.KickAttack.NAME, damage=1, combination="K")
    ]
    arnaldor_shuatseneguer_attacks = [
        Attack(name=constants.RemuyukenAttack.NAME, damage=3, combination="SA+K"),
        Attack(name=constants.TaladokenAttack.NAME, damage=2, combination="ASA+P"),
        Attack(name=constants.PunchAttack.NAME, damage=1, combination="P"),
        Attack(name=constants.KickAttack.NAME, damage=1, combination="K")
    ]

    player1_name = constants.TonynStalloneFighter.NAME
    player1_attacks = tonyn_stallone_attacks

    player2_name = constants.ArnaldorShuatseneguerFighter.NAME
    player2_attacks = arnaldor_shuatseneguer_attacks

    if not tonyn_starts:
        player1_name, player2_name = player2_name, player1_name
        player1_attacks, player2_attacks = player2_attacks, player1_attacks

    player1 = Fighter(name=player1_name, attacks=player1_attacks)
    player2 = Fighter(name=player2_name, attacks=player2_attacks)

    return player1, player2


def get_players_and_turns(kombat_data: dict) -> tuple[Fighter, Fighter, list, list]:
    tonyn_turns, arnaldor_turns, tonyn_starts = get_players_turns_and_define_starting_player(
        kombat_data=kombat_data
    )
    player1, player2 = create_players(tonyn_starts=tonyn_starts)

    player1_turns, player2_turns = (
        tonyn_turns,
        arnaldor_turns,
    ) if tonyn_starts else (arnaldor_turns, tonyn_turns)

    return player1, player2, player1_turns, player2_turns
