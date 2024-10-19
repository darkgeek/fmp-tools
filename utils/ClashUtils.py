from model.Lineup import Lineup, LineupPlayer
from model.Player import Player
from model.ClashReport import ClashReport
from model.AttackingStyle import AttackingStyle
from utils.PlayerUtils import get_by_no, get_by_pos, get_by_pos_list

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

    "fr-fil-pac-attack": 0.25,
    "fr-fil-tec-attack": 0.5,
    "fr-fil-pas-attack": 0.5,
    "fr-fil-pos-attack": 0.6,
    "fr-fil-hea-attack": 0.25,

    "dc-fil-mar-defend": 0.55,
    "dc-fil-tak-defend": 0.55,
    "dc-fil-pos-defend": 0.55,
    "dc-fil-hea-defend": 0.55,

    "dl-fil-mar-defend": 0.55,
    "dl-fil-tak-defend": 0.55,
    "dl-fil-pos-defend": 0.55,
    "dl-fil-hea-defend": 0.55,

    "dr-fil-mar-defend": 0.55,
    "dr-fil-tak-defend": 0.55,
    "dr-fil-pos-defend": 0.55,
    "dr-fil-hea-defend": 0.55,

    "mc-fil-mar-defend": 0.9,
    "mc-fil-tak-defend": 0.6,
    "mc-fil-pos-defend": 0.9,

    "ml-fil-pac-defend": 0.25,
    "ml-fil-mar-defend": 0.9,
    "ml-fil-tak-defend": 0.55,
    "ml-fil-pos-defend": 0.55,

    "mr-fil-pac-defend": 0.25,
    "mr-fil-mar-defend": 0.9,
    "mr-fil-tak-defend": 0.55,
    "mr-fil-pos-defend": 0.55,

    "fc-fil-mar-defend": 0.9,
    "fc-fil-tak-defend": 0.8,
    "fc-fil-pos-defend": 0.55,

    "fl-fil-pac-defend": 0.3,
    "fl-fil-mar-defend": 0.9,
    "fl-fil-tak-defend": 0.55,
    "fl-fil-pos-defend": 0.25,

    "fr-fil-pac-defend": 0.3,
    "fr-fil-mar-defend": 0.9,
    "fr-fil-tak-defend": 0.55,
    "fr-fil-pos-defend": 0.25,
}

OUTFIELDER_SKILLS = ["pac", "mar", "tak", "tec",
                     "pas", "pos", "cro", "hea", "fin", "lon"]
ZONES = ["dc", "dl", "dr", "mc", "ml", "mr", "fc", "fl", "fr"]
ZONE_TO_ATTACKER_POS_DICT = {
    "dc": ["dc", "dmc", "mc"],
    "dl": ["dl", "dml", "ml"],
    "dr": ["dr", "dmr", "mr"],
    "mc": ["mc", "dmc", "amc"],
    "ml": ["ml", "dml", "aml"],
    "mr": ["mr", "dmr", "amr"],
    "fc": ["fc", "amc", "mc"],
    "fl": ["fl", "aml", "ml"],
    "fr": ["fr", "amr", "mr"],
}
ATTACKER_ZONE_TO_DEFENDER_ZONE_DICT = {
    "dc": "fc",
    "dl": "fr",
    "dr": "fl",
    "mc": "mc",
    "ml": "mr",
    "mr": "ml",
    "fc": "dc",
    "fl": "dr",
    "fr": "dl",
}


def buildClashReport(attackers: [LineupPlayer], defenders: [LineupPlayer], style: AttackingStyle, allAttackers: [Player], allDefenders: [Player]) -> [ClashReport]:
    reports = []

    for zone in ZONES:
        attacker_pos_list = ZONE_TO_ATTACKER_POS_DICT[zone]
        aPlayers = get_by_pos_list(attacker_pos_list, attackers)

        defender_pos_list = ZONE_TO_ATTACKER_POS_DICT[ATTACKER_ZONE_TO_DEFENDER_ZONE_DICT[zone]]
        dPlayers = get_by_pos_list(defender_pos_list, defenders)

        for ap in aPlayers:
            fullAp = get_by_no(ap.no, allAttackers)
            for dp in dPlayers:
                fullDp = get_by_no(dp.no, allDefenders)

                report = buildOneOnOneClashReport(
                    fullAp, ap.position, fullDp, dp.position, style, zone)
                reports.append(report)

    return reports


def buildOneOnOneClashReport(attacker: Player, attackerPosition: str, defender: Player, defenderPosition: str, style: AttackingStyle, zone: str) -> ClashReport:
    attackerTacticGrade = getPlayerTacticsGrade(attacker, style, zone, True)
    defenderTacticGrade = getPlayerTacticsGrade(defender, style, zone, False)

    return ClashReport(zone=zone, attacker=attacker.name, attacker_pos=attackerPosition, attacker_energy=attacker.form,  attacker_overall_grade=attacker.rating, attacker_tactic_grade=attackerTacticGrade, defender=defender.name, defender_pos=defenderPosition, defender_energy=defender.form, defender_overall_grade=defender.rating, defender_tactic_grade=defenderTacticGrade)


def getPlayerTacticsGrade(player: Player, style: AttackingStyle, zone: str, is_attacking: bool) -> float:
    grade = 0

    direction = "attack" if is_attacking else "defend"
    style = style.name.lower()

    for sk in OUTFIELDER_SKILLS:
        grade = grade + CLASH_ZONE_AND_STYLE_AND_SKILL_AND_IS_ATTACKING_TO_WEIGHT_DICT.get(
            zone + "-" + style + "-" + sk + "-" + direction, 0) * getattr(player, sk)

    return grade
