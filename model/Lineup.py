from dataclasses import dataclass
from enum import Enum


@dataclass
class LineupPlayer:
    no: int
    position: str


@dataclass
class Lineup:
    players: [LineupPlayer]
