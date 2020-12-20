from __future__ import annotations
from typing import List
from dataclasses import dataclass, field
import random

from domain.enums import EnergyToken


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

    def roll(self) -> DiceOutcome:
        face = random.choice(self.faces)
        return DiceOutcome(face=face, dice=self)


@dataclass
class DiceOutcome:
    face: Face
    dice: Dice
