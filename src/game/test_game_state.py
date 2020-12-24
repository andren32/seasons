from typing import List

import pytest

from game.game_state import GameState, PlayerAction, PlayerActionType


def _assert_player_choose_dice_action(action: PlayerAction, player_id: int) -> None:
    assert action.player_id == player_id
    assert action.action_type == PlayerActionType.CHOOSE_DICE


def _assert_player_turn_action(action: PlayerAction, player_id: int) -> None:
    assert action.player_id == player_id
    assert action.action_type == PlayerActionType.PLAYER_TURN


@pytest.mark.parametrize(
    "expected_player_order", [[0, 1, 2, 3], [1, 2, 3, 0], [2, 3, 0, 1], [3, 0, 1, 2]]
)
def test_setup_round_sets_stack_in_correct_order(
    expected_player_order: List[int],
) -> None:
    gs = GameState(num_player=4)

    gs.first_player_id = expected_player_order[0]
    assert gs.player_actions == []

    gs.setup_round()

    for player_id in expected_player_order:
        _assert_player_choose_dice_action(gs.get_current_action(), player_id)
        gs.resolve_current_action()

    for player_id in expected_player_order:
        _assert_player_turn_action(gs.get_current_action(), player_id)
        gs.resolve_current_action()
