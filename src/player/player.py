from typing import List, Optional

from dice.dice import DiceOutcome
from domain.enums import EnergyToken
from cards.card import Card


class PlayerHand:
    # TODO: Probably should change to dict, id will change on removal
    hand: List[Card]

    def __init__(self) -> None:
        self.hand = []

    def add(self, card: Card) -> None:
        self.hand.append(card)

    def add_multiple(self, cards: List[Card]) -> None:
        self.hand += cards

    def remove(self, card_id: int) -> Card:
        return self.hand.pop(card_id)

    def set_hand(self, hand: List[Card]) -> None:
        self.hand = hand


class Player:
    player_id: int
    stars: int
    crystals: int
    used_bonuses: int
    tokens: List[EnergyToken]
    chosen_dice: Optional[DiceOutcome]
    hand: PlayerHand
    summoned_cards: List[Card]
    library_2: List[Card]
    library_3: List[Card]

    def __init__(self, player_id: int) -> None:
        self.player_id = player_id
        self.stars = 0
        self.crystals = 0
        self.used_bonuses = 0
        self.tokens = []
        self.chosen_dice = None

        self.hand = PlayerHand()
        self.summoned_cards = []
        self.library_2 = []
        self.library_3 = []

    def setup_starting_cards(
        self, hand: List[Card], lib_2: List[Card], lib_3: List[Card]
    ) -> None:
        assert len(hand) == 3
        assert len(lib_2) == 3
        assert len(lib_3) == 3

        self.hand.set_hand(hand)
        self.library_2 = lib_2
        self.library_3 = lib_3

    def set_chosen_dice(self, dice: Optional[DiceOutcome]) -> None:
        self.chosen_dice = dice
