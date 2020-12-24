from enum import Enum
from typing import List, Dict
import random

from dice.dice import Dice, Face, DiceOutcome
from domain.enums import Season, EnergyToken


def _get_tokens_for_season(season: Season) -> List[EnergyToken]:
    tokens_per_season = {
        Season.WINTER: [EnergyToken.WATER, EnergyToken.AIR, EnergyToken.FIRE],
        Season.SPRING: [EnergyToken.EARTH, EnergyToken.WATER, EnergyToken.AIR],
        Season.SUMMER: [EnergyToken.FIRE, EnergyToken.EARTH, EnergyToken.WATER],
        Season.AUTUMN: [EnergyToken.AIR, EnergyToken.FIRE, EnergyToken.EARTH],
    }
    return tokens_per_season[season]


def _create_dice_set(
    primary: EnergyToken, secondary: EnergyToken, uncommon: EnergyToken
) -> List[Dice]:
    return [
        Dice(
            [
                Face(pips=1, draw=True),
                Face(pips=3, crystals=3, tokens=[primary, primary]),
                Face(pips=1, star=True, tokens=[primary, primary]),
                Face(pips=2, star=True, tokens=[uncommon]),
                Face(pips=2, star=True, transmute=True, tokens=[secondary]),
                Face(pips=3, transmute=True, tokens=[primary, secondary]),
            ]
        ),
        Dice(
            [
                Face(pips=2, draw=True),
                Face(pips=1, crystals=3, tokens=[primary, primary]),
                Face(pips=2, star=True, tokens=[primary, primary]),
                Face(pips=3, star=True, tokens=[secondary, secondary]),
                Face(pips=3, star=True, transmute=True, tokens=[uncommon]),
                Face(pips=1, transmute=True, tokens=[primary, secondary]),
            ]
        ),
        Dice(
            [
                Face(pips=3, draw=True),
                Face(pips=2, crystals=1, tokens=[primary, primary]),
                Face(pips=3, star=True, tokens=[primary, primary]),
                Face(pips=1, star=True, tokens=[uncommon, uncommon]),
                Face(pips=1, star=True, transmute=True, tokens=[secondary]),
                Face(pips=2, transmute=True, tokens=[primary, secondary]),
            ]
        ),
        Dice(
            [
                Face(pips=2, crystals=6),
                Face(pips=2, crystals=2, tokens=[primary, primary]),
                Face(pips=1, star=True, tokens=[primary, primary]),
                Face(pips=3, star=True, tokens=[uncommon]),
                Face(pips=3, star=True, transmute=True, tokens=[secondary]),
                Face(pips=1, transmute=True, tokens=[primary, secondary]),
            ]
        ),
        Dice(
            [
                Face(pips=3, crystals=6),
                Face(pips=2, crystals=1, tokens=[primary, primary]),
                Face(pips=3, star=True, tokens=[primary, primary]),
                Face(pips=1, star=True, tokens=[uncommon]),
                Face(pips=1, star=True, transmute=True, tokens=[secondary]),
                Face(pips=2, transmute=True, tokens=[secondary, secondary]),
            ]
        ),
    ]


class DiceSet:
    dices: List[Dice]

    def __init__(self, season: Season, num_dice: int):
        assert 0 < num_dice <= 5

        primary, secondary, uncommon = _get_tokens_for_season(season)
        dices = _create_dice_set(primary, secondary, uncommon)

        self.dices = random.sample(dices, k=num_dice)

    def roll(self) -> List[DiceOutcome]:
        return [d.roll() for d in self.dices]


class SeasonDiceSet:
    dice_per_season: Dict[Season, DiceSet]

    def __init__(self, num_dice: int) -> None:
        self.dice_per_season = {
            Season.WINTER: DiceSet(Season.WINTER, num_dice),
            Season.SPRING: DiceSet(Season.SPRING, num_dice),
            Season.SUMMER: DiceSet(Season.SUMMER, num_dice),
            Season.AUTUMN: DiceSet(Season.AUTUMN, num_dice),
        }

    def roll_for_season(self, season: Season) -> List[DiceOutcome]:
        return self.dice_per_season[season].roll()
