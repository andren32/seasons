import random

from typing import List
from cards.card import Card
from cards.empty_card import EmptyCard


class Deck:
    cards: List[Card]

    def __init__(self) -> None:
        self.cards = [EmptyCard() for _ in range(100)]
        random.shuffle(self.cards)

    def draw_cards(self, num_cards: int) -> List[Card]:
        drawn_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return drawn_cards