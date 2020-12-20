import random
from cards.card import Card


class EmptyCard(Card):
    i = 0

    def __init__(self) -> None:
        self.name = f"Random Empty card of Doom {EmptyCard.i}"
        EmptyCard.i += 1
        self.points = random.randint(0, 5)
        self.can_activate = False

    def on_before_summon(self) -> None:
        pass

    def on_summon(self) -> None:
        pass

    def on_activate(self) -> None:
        pass

    def on_round_end(self) -> None:
        pass

    def on_season_end(self) -> None:
        pass

    def on_game_end(self) -> None:
        pass