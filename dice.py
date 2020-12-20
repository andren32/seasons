from enum import Enum
from typing import List
from dataclasses import dataclass, field
import random


class EnergyToken(Enum):
    WIND = 1
    FIRE = 2
    EARTH = 3
    WATER = 4


@dataclass
class Face:
    pips: int
    crystals: int = 0
    tokens: List[EnergyToken] = field(default_factory=list)
    transmute: bool = False
    star: bool = False
    draw: bool = False


class Dice:
    faces: List[Face]

    def __init__(self, faces: List[Face]):
        assert len(faces) == 6

        self.faces = faces

    def roll(self) -> Face:
        face = random.choice(self.faces)
        return face


def create_dice_set(
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


(dice,) = create_dice_set(EnergyToken.WATER, EnergyToken.WIND, EnergyToken.FIRE)
print(dice.roll())
