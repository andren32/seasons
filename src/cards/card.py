from abc import ABC, abstractmethod


class Card(ABC):
    name: str = "Abstract"
    description: str = "Card description"
    points: int = 0
    can_activate: bool = False

    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return (
            f"Card({self.name}, points={self.points}, can_activate={self.can_activate})"
        )

    @abstractmethod
    def on_before_summon(self) -> None:
        pass

    @abstractmethod
    def on_summon(self) -> None:
        pass

    @abstractmethod
    def on_activate(self) -> None:
        pass

    @abstractmethod
    def on_round_end(self) -> None:
        pass

    @abstractmethod
    def on_season_end(self) -> None:
        pass

    @abstractmethod
    def on_game_end(self) -> None:
        pass
