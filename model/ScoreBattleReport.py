from dataclasses import dataclass
from model.KickStyle import KickStyle


@dataclass
class ScoreBattleReport:
    score_method_grade: float

    gk_energy: float
    gk_overall_grade: float
    gk_tactic_grade: float
