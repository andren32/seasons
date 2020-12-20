import pytest
from dice.dice_set import DiceSet, Season


@pytest.mark.parametrize(
    "season", [Season.WINTER, Season.SPRING, Season.SUMMER, Season.AUTUMN]
)
def test_can_make_dice_set_for_every_season(season: Season) -> None:
    assert len(DiceSet(season, 4).dices) == 4
