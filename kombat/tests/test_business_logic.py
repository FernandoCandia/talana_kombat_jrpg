from unittest.mock import Mock, patch

import pytest

from kombat.business_logic import (
    create_players,
    get_player_data_to_initialize_kombat,
    get_players_turns_and_define_starting_player, get_players_and_turns,
)
from kombat.fighters import Fighter, Attack
from kombat.lib import constants


@pytest.mark.parametrize(
    "player_data, expected_player_turns, expected_combinations_count, expected_movements_count, expected_hit_counts",
    [
        (
            {"movimientos": ["D", "DSD", "S", "DSD", "SD"], "golpes": ["K", "P", "", "K", "P"]},
            ["D+K", "DSD+P", "S+", "DSD+K", "SD+P"],
            4,
            10,
            4
        ),
        (
            {"movimientos": ["SA", "SA", "SA", "ASA", "SA"], "golpes": ["K", "", "K", "P", "P"]},
            ["SA+K", "SA+", "SA+K", "ASA+P", "SA+P"],
            4,
            11,
            4
        ),
        (
            {"movimientos": ["", "DSD", "", "", "SD"], "golpes": ["", "", "", "", ""]},
            ["", "DSD+", "", "", "SD+"],
            0,
            5,
            0
        )
    ]
)
def test_get_player_data_to_initialize_kombat(
    player_data,
    expected_player_turns,
    expected_combinations_count,
    expected_movements_count,
    expected_hit_counts
):
    player_turns, combinations_count, movements_count, hit_counts = get_player_data_to_initialize_kombat(
        player_data
    )

    assert player_turns == expected_player_turns
    assert combinations_count == expected_combinations_count
    assert movements_count == expected_movements_count
    assert hit_counts == expected_hit_counts


@pytest.mark.parametrize(
    "kombat_data, expected_tonyn_turns, expected_arnaldor_turns, expected_starting_player",
    [
        (
            {
                "player1": {
                    "movimientos": ["D", "DSD", "S", "DSD", "SD"],
                    "golpes": ["K", "P", "", "K", "P"]
                },
                "player2": {
                    "movimientos": ["SA", "SA", "SA", "ASA", "SA"],
                    "golpes": ["K", "", "K", "P", "P"]
                }
            },
            ["D+K", "DSD+P", "S+", "DSD+K", "SD+P"],
            ["SA+K", "SA+", "SA+K", "ASA+P", "SA+P"],
            True
        ),
        (
            {
                "player1": {
                    "movimientos": ["A", "A", "A", "A", "A"],
                    "golpes": ["P", "P", "P", "P", "P"]
                },
                "player2": {
                    "movimientos": ["S", "S", "S", "S", "S"],
                    "golpes": ["K", "K", "K", "K", "K"]
                }
            },
            ["A+P", "A+P", "A+P", "A+P", "A+P"],
            ["S+K", "S+K", "S+K", "S+K", "S+K"],
            True
        ),
        (
            {
                "player1": {
                    "movimientos": ["", "", "", "", ""],
                    "golpes": ["", "", "", "", ""]
                },
                "player2": {
                    "movimientos": ["", "", "", "", ""],
                    "golpes": ["", "", "", "", ""]
                }
            },
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            True
        ),
        (
            {
                "player1": {
                    "movimientos": ["D", "", "S", "", "SD"],
                    "golpes": ["K", "P", "", "", ""]
                },
                "player2": {
                    "movimientos": ["", "SA", "", "ASA", ""],
                    "golpes": ["", "", "K", "P", "P"]
                }
            },
            ["D+K", "+P", "S+", "", "SD+"],
            ["", "SA+", "+K", "ASA+P", "+P"],
            True
        ),
    ]
)
def test_get_players_turns_and_define_starting_player(
    kombat_data,
    expected_tonyn_turns,
    expected_arnaldor_turns,
    expected_starting_player
):
    tonyn_turns, arnaldor_turns, starting_player = get_players_turns_and_define_starting_player(kombat_data)

    assert tonyn_turns == expected_tonyn_turns
    assert arnaldor_turns == expected_arnaldor_turns
    assert starting_player == expected_starting_player


@pytest.mark.parametrize("tonyn_starts", [True, False])
def test_create_players(mocker, tonyn_starts):
    create_players_mock = mocker.Mock(
        return_value=(
            Fighter(name=constants.TonynStalloneFighter.NAME, attacks=mocker.Mock()),
            Fighter(name=constants.ArnaldorShuatseneguerFighter.NAME, attacks=mocker.Mock())
        )
    )

    with patch("kombat.business_logic.create_players", create_players_mock):
        player1, player2 = create_players(tonyn_starts)

    if tonyn_starts:
        assert player1.name == constants.TonynStalloneFighter.NAME
        assert player2.name == constants.ArnaldorShuatseneguerFighter.NAME
    else:
        assert player1.name == constants.ArnaldorShuatseneguerFighter.NAME
        assert player2.name == constants.TonynStalloneFighter.NAME


@pytest.mark.parametrize("tonyn_starts", [True, False])
def test_get_players_and_turns(tonyn_starts, mocker):
    get_players_turns_and_define_starting_player_mock = Mock(
        return_value=(
            ["D", "DSD", "S", "DSD", "SD"],
            ["SA", "SA", "SA", "ASA", "SA"],
            tonyn_starts
        )
    )

    create_players_mock = Mock(
        return_value=(
            Fighter(name="Tonyn Stallone"),
            Fighter(name="Arnaldor Shuatseneguer")
        )
    )

    mocker.patch(
        "kombat.business_logic.get_players_turns_and_define_starting_player",
        get_players_turns_and_define_starting_player_mock,
    )
    mocker.patch("kombat.business_logic.create_players", create_players_mock)

    player1, player2, player1_turns, player2_turns = get_players_and_turns({
        "player1": {"movimientos": ["D", "DSD", "S", "DSD", "SD"], "golpes": ["K", "P", "", "K", "P"]},
        "player2": {"movimientos": ["SA", "SA", "SA", "ASA", "SA"], "golpes": ["K", "", "K", "P", "P"]}
    })

    get_players_turns_and_define_starting_player_mock.assert_called_once_with(kombat_data={
        "player1": {"movimientos": ["D", "DSD", "S", "DSD", "SD"], "golpes": ["K", "P", "", "K", "P"]},
        "player2": {"movimientos": ["SA", "SA", "SA", "ASA", "SA"], "golpes": ["K", "", "K", "P", "P"]}
    })
    create_players_mock.assert_called_once_with(tonyn_starts=tonyn_starts)

    assert player1.name == "Tonyn Stallone"
    assert player2.name == "Arnaldor Shuatseneguer"
    assert player1_turns == ["D", "DSD", "S", "DSD", "SD"] if tonyn_starts else ["SA", "SA", "SA", "ASA", "SA"]
    assert player2_turns == ["SA", "SA", "SA", "ASA", "SA"] if tonyn_starts else ["D", "DSD", "S", "DSD", "SD"]
