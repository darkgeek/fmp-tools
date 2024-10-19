from dataclasses import dataclass
from model.KickStyle import KickStyle


@dataclass
class KickingBattleReport:
    style: KickStyle
    possibility: float

    attacker: str
    attacker_pos: str
    attacker_energy: float
    attacker_overall_grade: float
    attacker_tactic_grade: float

    defender: str
    defender_pos: str
    defender_energy: float
    defender_overall_grade: float
    defender_tactic_grade: float
