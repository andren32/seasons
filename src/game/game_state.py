from typing import List
from player.player import Player
from cards.deck import Deck
from dice.dice_set import SeasonDiceSet


class GameState:
    first_player: int
    players: List[Player]
    deck: Deck
    dice: SeasonDiceSet
    year: int
    month: int

    def __init__(self, num_player: int):
        assert 0 < num_player <= 4
        self.first_player = 0
        self.players = [Player() for _ in range(num_player)]
        self.deck = Deck()
        self.dice = SeasonDiceSet(num_dice=num_player + 1)
        self.year = 1
        self.month = 1

        self._simulate_prelude()

    def _simulate_prelude(self) -> None:
        for player in self.players:
            drawn = self.deck.draw_cards(9)
            player.hand.add_multiple(drawn[:3])
            player.library_2 = drawn[3:6]
            player.library_3 = drawn[6:9]
