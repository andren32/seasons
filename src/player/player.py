from typing import List
from domain.enums import EnergyToken
from cards.card import Card


class PlayerHand:
    hand: List[Card]

    def __init__(self) -> None:
        self.hand = []

    def add(self, card: Card) -> None:
        self.hand.append(card)

    def add_multiple(self, cards: List[Card]) -> None:
        self.hand += cards

    def remove(self, id: int) -> Card:
        return self.hand.pop(id)


class Player:
    stars: int
    crystals: int
    used_bonuses: int
    tokens: List[EnergyToken]
    hand: PlayerHand
    summoned_cards: List[Card]
    library_2: List[Card]
    library_3: List[Card]

    def __init__(self) -> None:
        self.stars = 0
        self.crystals = 0
        self.used_bonuses = 0
        self.tokens = []

        self.hand = PlayerHand()
        self.summoned_cards = []
        self.library_2 = []
        self.library_3 = []