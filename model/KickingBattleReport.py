from dataclasses import dataclass
from model.KickStyle import KickStyle


@dataclass
class KickingBattleReport:
    attacker: str
    attacker_pos: str
    attacker_energy: float
    attacker_overall_grade: float

    defender: str
    defender_pos: str
    defender_energy: float
    defender_overall_grade: float

    duel_win_possibilities: []

    gk_energy: float
    gk_overall_grade: float
