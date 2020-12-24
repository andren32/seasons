from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from dice.dice import DiceOutcome
from domain.enums import Season
from player.player import Player
from cards.deck import Deck
from dice.dice_set import SeasonDiceSet


class PlayerActionType(Enum):
    CHOOSE_DICE = 1
    PLAYER_TURN = 2


@dataclass
class PlayerAction:
    player_id: int
    action_type: PlayerActionType


class GameState:
    first_player_id: int
    players: List[Player]
    deck: Deck
    dice: SeasonDiceSet
    leftover_dice: Optional[DiceOutcome]
    year: int
    month: int
    player_actions: List[PlayerAction]

    def __init__(self, num_player: int):
        assert 0 < num_player <= 4
        self.first_player_id = 0
        self.players = [Player(player_id=i) for i in range(num_player)]
        self.deck = Deck()
        self.dice = SeasonDiceSet(num_dice=num_player + 1)
        self.leftover_dice = None
        self.year = 0
        self.month = 0

        # player actions is a stack of actions that players are required to perform
        self.player_actions = []

        self._simulate_prelude()

    def _simulate_prelude(self) -> None:
        for player in self.players:
            drawn = self.deck.draw_cards(9)
            player.hand.add_multiple(drawn[:3])
            player.library_2 = drawn[3:6]
            player.library_3 = drawn[6:9]

    def _clear_dice(self) -> None:
        for player in self.players:
            player.set_chosen_dice(None)
        self.leftover_dice = None

    def _players_in_player_order(self) -> List[Player]:
        return (
            self.players[self.first_player_id :] + self.players[: self.first_player_id]
        )

    def _add_player_action(self, action: PlayerAction) -> None:
        self.player_actions.append(action)

    def _add_dice_actions(self) -> None:
        for player in reversed(self._players_in_player_order()):
            self._add_player_action(
                PlayerAction(player.player_id, PlayerActionType.CHOOSE_DICE)
            )

    def _add_player_turns(self) -> None:
        for player in reversed(self._players_in_player_order()):
            self._add_player_action(
                PlayerAction(player.player_id, PlayerActionType.PLAYER_TURN)
            )

    def setup_round(self) -> None:
        self._add_player_turns()
        self._add_dice_actions()

    def is_player_actions_pending(self) -> bool:
        return len(self.player_actions) > 0

    def get_current_action(self) -> PlayerAction:
        assert len(self.player_actions) > 0
        return self.player_actions[-1]

    def resolve_current_action(self) -> None:
        self.player_actions.pop()

    def move_time(self, units: int) -> None:
        assert abs(units) <= 3
        self.month += units

        if self.month >= 12:
            self.year += 1
            self.month = self.month % 12
        elif self.month < 0:
            self.month += 12
            self.year = max(self.year - 1, 0)

    def end_of_round(self) -> None:
        assert self.leftover_dice is not None
        self.move_time(self.leftover_dice.face.pips)
        self._clear_dice()
        self.first_player_id = (self.first_player_id + 1) % len(self.players)

    def is_game_over(self) -> bool:
        return self.year == 2

    def current_season(self) -> Season:
        if 0 <= self.month <= 2:
            return Season.SPRING
        elif 3 <= self.month <= 5:
            return Season.SUMMER
        elif 6 <= self.month <= 8:
            return Season.AUTUMN
        else:
            return Season.WINTER

    def roll_current_dice(self) -> List[DiceOutcome]:
        return self.dice.roll_for_season(self.current_season())
