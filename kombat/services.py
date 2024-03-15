from itertools import zip_longest

from kombat import business_logic as kombat_business_logic


def get_kombat_result(kombat_data: dict) -> list[str]:
    kombat_result = []

    player1, player2, player1_turns, player2_turns = kombat_business_logic.get_players_and_turns(
        kombat_data=kombat_data
    )

    combined_turns = []
    for turn1, turn2 in zip_longest(player1_turns, player2_turns, fillvalue=None):
        combined_turns.append((player1, turn1)) if turn1 is not None else None
        combined_turns.append((player2, turn2)) if turn2 is not None else None

    for player, player_turn in combined_turns:
        opponent = player2 if player == player1 else player1

        if player.energy_points <= 0 or opponent.energy_points <= 0:
            break

        message, damage = player.make_move(player_turn)
        kombat_result.append(message)
        opponent.energy_points -= damage

    winner = player1 if player1.energy_points > player2.energy_points else player2
    kombat_result.append(f"{winner.name} gana la pelea y aún le queda {winner.energy_points} de energía!")

    return kombat_result
