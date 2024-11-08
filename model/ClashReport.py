from dataclasses import dataclass


@dataclass
class ClashReport:
    zone: str

    attacker: str
    attacker_pos: str
    attacker_energy: float
    attacker_overall_grade: float

    win_possibilities: []

    defender: str
    defender_pos: str
    defender_energy: float
    defender_overall_grade: float
