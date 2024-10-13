from model.Player import Player
from model.ClashReport import ClashReport

CLASH_ZONE_AND_STYLE_AND_SKILL_AND_IS_ATTACKING_TO_WEIGHT_DICT = {
    "dc-fil-tec-attack": 0.9,
    "dc-fil-pas-attack": 0.85,
    "dc-fil-lon-attack": 0.3,

    "dl-fil-pac-attack": 0.25,
    "dl-fil-tec-attack": 0.55,
    "dl-fil-pas-attack": 0.7,
    "dl-fil-cro-attack": 0.25,
    "dl-fil-lon-attack": 0.3,

    "dr-fil-pac-attack": 0.25,
    "dr-fil-tec-attack": 0.55,
    "dr-fil-pas-attack": 0.7,
    "dr-fil-cro-attack": 0.25,
    "dr-fil-lon-attack": 0.3,

    "mc-fil-tec-attack": 0.85,
    "mc-fil-pas-attack": 1.0,
    "mc-fil-pos-attack": 0.25,

    "ml-fil-pac-attack": 0.4,
    "ml-fil-tec-attack": 0.5,
    "ml-fil-pas-attack": 0.85,
    "ml-fil-cro-attack": 0.45,

    "mr-fil-pac-attack": 0.4,
    "mr-fil-tec-attack": 0.5,
    "mr-fil-pas-attack": 0.85,
    "mr-fil-cro-attack": 0.45,

    "fc-fil-pac-attack": 0.25,
    "fc-fil-tak-attack": 0.45,
    "fc-fil-tec-attack": 0.25,
    "fc-fil-pas-attack": 0.25,
    "fc-fil-pos-attack": 0.5,
    "fc-fil-hea-attack": 0.5,

    "fl-fil-pac-attack": 0.25,
    "fl-fil-tec-attack": 0.5,
    "fl-fil-pas-attack": 0.5,
    "fl-fil-pos-attack": 0.6,
    "fl-fil-hea-attack": 0.25,
}

OUTFIELDER_SKILLS = ["pac", "mar", "tak", "tec",
                     "pas", "pos", "cro", "hea", "fin", "lon"]
ZONES = ["dc", "dl", "dr", "mc", "ml", "mr", "fc", "fl", "fr"]


def buildClashReport(attackers: [Player], defenders: [Player], style: AttackingStyle) -> [ClashReport]:
    return []


def buildOneOnOneClashReport(attacker: Player, defender: Player, style: AttackingStyle, zone: str) -> ClashReport:
    return


def getPlayerTacticsGrade(player: Player, style: AttackingStyle, zone: str, is_attacking: bool) -> float:
    grade = 0

    direction = "attack" if is_attacking else "defend"
    style = style.name.lower()

    for sk in OUTFIELDER_SKILLS:
        grade = grade + CLASH_ZONE_AND_STYLE_AND_SKILL_AND_IS_ATTACKING_TO_WEIGHT_DICT.get(
            zone + "-" + style + "-" + sk + "-" + direction, 0) * getattr(player, sk)

    return grade
