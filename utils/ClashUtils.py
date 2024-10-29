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

    "dc-sho-tec-attack": 0.95,
    "dc-sho-pas-attack": 0.75,
    "dc-sho-pos-attack": 0.3,

    "dl-sho-tec-attack": 0.6,
    "dl-sho-pas-attack": 0.75,
    "dl-sho-pos-attack": 0.3,
    "dl-sho-cro-attack": 0.25,

    "dr-sho-tec-attack": 0.6,
    "dr-sho-pas-attack": 0.75,
    "dr-sho-pos-attack": 0.3,
    "dr-sho-cro-attack": 0.25,

    "mc-sho-tec-attack": 0.7,
    "mc-sho-pas-attack": 0.95,
    "mc-sho-pos-attack": 0.3,

    "ml-sho-tec-attack": 0.55,
    "ml-sho-pas-attack": 0.8,
    "ml-sho-pos-attack": 0.25,
    "ml-sho-cro-attack": 0.45,

    "mr-sho-tec-attack": 0.55,
    "mr-sho-pas-attack": 0.8,
    "mr-sho-pos-attack": 0.25,
    "mr-sho-cro-attack": 0.45,

    "fc-sho-pac-attack": 0.15,
    "fc-sho-tec-attack": 0.55,
    "fc-sho-pas-attack": 0.55,
    "fc-sho-pos-attack": 0.55,
    "fc-sho-hea-attack": 0.25,

    "fl-sho-pac-attack": 0.15,
    "fl-sho-tec-attack": 0.55,
    "fl-sho-pas-attack": 0.55,
    "fl-sho-pos-attack": 0.55,
    "fl-sho-hea-attack": 0.25,

    "fr-sho-pac-attack": 0.15,
    "fr-sho-tec-attack": 0.55,
    "fr-sho-pas-attack": 0.55,
    "fr-sho-pos-attack": 0.55,
    "fr-sho-hea-attack": 0.25,

    "dc-sho-mar-defend": 0.5,
    "dc-sho-tak-defend": 0.3,
    "dc-sho-pos-defend": 0.7,
    "dc-sho-hea-defend": 0.3,

    "dl-sho-pac-defend": 0.3,
    "dl-sho-mar-defend": 0.5,
    "dl-sho-tak-defend": 0.75,
    "dl-sho-pos-defend": 0.35,

    "dr-sho-pac-defend": 0.3,
    "dr-sho-mar-defend": 0.5,
    "dr-sho-tak-defend": 0.75,
    "dr-sho-pos-defend": 0.35,

    "mc-sho-mar-defend": 0.7,
    "mc-sho-tak-defend": 0.55,
    "mc-sho-pos-defend": 0.7,

    "ml-sho-pac-defend": 0.3,
    "ml-sho-mar-defend": 0.7,
    "ml-sho-tak-defend": 0.5,
    "ml-sho-pos-defend": 0.5,

    "mr-sho-pac-defend": 0.3,
    "mr-sho-mar-defend": 0.7,
    "mr-sho-tak-defend": 0.5,
    "mr-sho-pos-defend": 0.5,

    "fc-sho-mar-defend": 0.7,
    "fc-sho-tak-defend": 0.8,
    "fc-sho-pos-defend": 0.5,

    "fl-sho-pac-defend": 0.4,
    "fl-sho-mar-defend": 0.7,
    "fl-sho-tak-defend": 0.5,
    "fl-sho-pos-defend": 0.35,

    "fr-sho-pac-defend": 0.4,
    "fr-sho-mar-defend": 0.7,
    "fr-sho-tak-defend": 0.5,
    "fr-sho-pos-defend": 0.35,

    "dc-lon-tec-attack": 0.5,
    "dc-lon-pas-attack": 0.6,
    "dc-lon-lon-attack": 0.9,

    "dl-lon-pac-attack": 0.2,
    "dl-lon-tec-attack": 0.25,
    "dl-lon-pas-attack": 0.3,
    "dl-lon-cro-attack": 0.2,
    "dl-lon-lon-attack": 0.9,

    "dr-lon-pac-attack": 0.2,
    "dr-lon-tec-attack": 0.25,
    "dr-lon-pas-attack": 0.3,
    "dr-lon-cro-attack": 0.2,
    "dr-lon-lon-attack": 0.9,

    "mc-lon-pac-attack": 0.2,
    "mc-lon-tec-attack": 0.5,
    "mc-lon-pas-attack": 0.6,
    "mc-lon-lon-attack": 0.65,

    "ml-lon-pac-attack": 0.2,
    "ml-lon-tec-attack": 0.5,
    "ml-lon-pas-attack": 0.3,
    "ml-lon-cro-attack": 0.2,
    "ml-lon-lon-attack": 0.65,

    "mr-lon-pac-attack": 0.2,
    "mr-lon-tec-attack": 0.5,
    "mr-lon-pas-attack": 0.3,
    "mr-lon-cro-attack": 0.2,
    "mr-lon-lon-attack": 0.65,

    "fc-lon-pac-attack": 0.2,
    "fc-lon-tec-attack": 0.5,
    "fc-lon-pas-attack": 0.3,
    "fc-lon-pos-attack": 0.5,
    "fc-lon-hea-attack": 0.55,

    "fl-lon-pac-attack": 0.2,
    "fl-lon-tec-attack": 0.3,
    "fl-lon-pas-attack": 0.5,
    "fl-lon-pos-attack": 0.5,
    "fl-lon-cro-attack": 0.3,
    "fl-lon-hea-attack": 0.2,

    "fr-lon-pac-attack": 0.2,
    "fr-lon-tec-attack": 0.3,
    "fr-lon-pas-attack": 0.5,
    "fr-lon-pos-attack": 0.5,
    "fr-lon-cro-attack": 0.3,
    "fr-lon-hea-attack": 0.2,

    "dc-lon-mar-defend": 0.5,
    "dc-lon-tak-defend": 0.5,
    "dc-lon-pos-defend": 0.5,
    "dc-lon-hea-defend": 0.5,

    "dl-lon-mar-defend": 0.5,
    "dl-lon-tak-defend": 0.5,
    "dl-lon-pos-defend": 0.5,
    "dl-lon-hea-defend": 0.5,

    "dr-lon-mar-defend": 0.5,
    "dr-lon-tak-defend": 0.5,
    "dr-lon-pos-defend": 0.5,
    "dr-lon-hea-defend": 0.5,

    "mc-lon-pac-defend": 0.5,
    "mc-lon-mar-defend": 0.5,
    "mc-lon-tak-defend": 0.5,
    "mc-lon-pos-defend": 0.5,

    "ml-lon-pac-defend": 0.5,
    "ml-lon-mar-defend": 0.5,
    "ml-lon-tak-defend": 0.5,
    "ml-lon-pos-defend": 0.5,

    "mr-lon-pac-defend": 0.5,
    "mr-lon-mar-defend": 0.5,
    "mr-lon-tak-defend": 0.5,
    "mr-lon-pos-defend": 0.5,

    "fc-lon-pac-defend": 0.5,
    "fc-lon-mar-defend": 0.5,
    "fc-lon-tak-defend": 0.5,
    "fc-lon-pos-defend": 0.5,

    "fl-lon-pac-defend": 0.5,
    "fl-lon-mar-defend": 0.5,
    "fl-lon-tak-defend": 0.5,
    "fl-lon-pos-defend": 0.5,

    "fr-lon-pac-defend": 0.5,
    "fr-lon-mar-defend": 0.5,
    "fr-lon-tak-defend": 0.5,
    "fr-lon-pos-defend": 0.5,

    "dc-cou-pac-attack": 0.7,
    "dc-cou-tec-attack": 0.5,
    "dc-cou-pas-attack": 0.5,
    "dc-cou-pos-attack": 0.3,

    "dl-cou-pac-attack": 0.7,
    "dl-cou-tec-attack": 0.5,
    "dl-cou-pas-attack": 0.5,
    "dl-cou-pos-attack": 0.3,

    "dr-cou-pac-attack": 0.7,
    "dr-cou-tec-attack": 0.5,
    "dr-cou-pas-attack": 0.5,
    "dr-cou-pos-attack": 0.3,

    "mc-cou-pac-attack": 0.7,
    "mc-cou-tec-attack": 0.5,
    "mc-cou-pas-attack": 0.5,
    "mc-cou-pos-attack": 0.3,

    "ml-cou-pac-attack": 0.7,
    "ml-cou-tec-attack": 0.5,
    "ml-cou-pas-attack": 0.5,
    "ml-cou-pos-attack": 0.3,

    "mr-cou-pac-attack": 0.7,
    "mr-cou-tec-attack": 0.5,
    "mr-cou-pas-attack": 0.5,
    "mr-cou-pos-attack": 0.3,

    "fc-cou-pac-attack": 0.7,
    "fc-cou-tec-attack": 0.3,
    "fc-cou-pos-attack": 0.5,
    "fc-cou-hea-attack": 0.5,

    "fl-cou-pac-attack": 0.7,
    "fl-cou-tec-attack": 0.4,
    "fl-cou-pas-attack": 0.4,
    "fl-cou-pos-attack": 0.3,
    "fl-cou-hea-attack": 0.25,

    "fr-cou-pac-attack": 0.7,
    "fr-cou-tec-attack": 0.4,
    "fr-cou-pas-attack": 0.4,
    "fr-cou-pos-attack": 0.3,
    "fr-cou-hea-attack": 0.25,

    "dc-cou-mar-defend": 0.5,
    "dc-cou-tak-defend": 0.5,
    "dc-cou-pos-defend": 0.5,
    "dc-cou-hea-defend": 0.5,

    "dl-cou-mar-defend": 0.5,
    "dl-cou-tak-defend": 0.5,
    "dl-cou-pos-defend": 0.5,
    "dl-cou-hea-defend": 0.5,

    "dr-cou-mar-defend": 0.5,
    "dr-cou-tak-defend": 0.5,
    "dr-cou-pos-defend": 0.5,
    "dr-cou-hea-defend": 0.5,

    "mc-cou-pac-defend": 0.8,
    "mc-cou-mar-defend": 0.5,
    "mc-cou-tak-defend": 0.7,

    "ml-cou-pac-defend": 0.8,
    "ml-cou-mar-defend": 0.5,
    "ml-cou-tak-defend": 0.7,

    "mr-cou-pac-defend": 0.8,
    "mr-cou-mar-defend": 0.5,
    "mr-cou-tak-defend": 0.7,

    "fc-cou-pac-defend": 0.8,
    "fc-cou-mar-defend": 0.5,
    "fc-cou-tak-defend": 0.7,

    "fl-cou-pac-defend": 0.8,
    "fl-cou-mar-defend": 0.5,
    "fl-cou-tak-defend": 0.7,

    "fr-cou-pac-defend": 0.8,
    "fr-cou-mar-defend": 0.5,
    "fr-cou-tak-defend": 0.7,

    "dc-win-pac-attack": 0.35,
    "dc-win-tec-attack": 0.35,
    "dc-win-pas-attack": 0.6,
    "dc-win-pos-attack": 0.3,
    "dc-win-cro-attack": 0.5,

    "dl-win-pac-attack": 0.5,
    "dl-win-tec-attack": 0.35,
    "dl-win-pas-attack": 0.3,
    "dl-win-pos-attack": 0.35,
    "dl-win-cro-attack": 0.5,

    "dr-win-pac-attack": 0.5,
    "dr-win-tec-attack": 0.35,
    "dr-win-pas-attack": 0.3,
    "dr-win-pos-attack": 0.35,
    "dr-win-cro-attack": 0.5,

    "mc-win-pac-attack": 0.9,
    "mc-win-tec-attack": 0.4,
    "mc-win-pas-attack": 0.6,
    "mc-win-cro-attack": 0.3,

    "ml-win-pac-attack": 0.9,
    "ml-win-tec-attack": 0.35,
    "ml-win-pas-attack": 0.4,
    "ml-win-cro-attack": 0.4,

    "mr-win-pac-attack": 0.9,
    "mr-win-tec-attack": 0.35,
    "mr-win-pas-attack": 0.4,
    "mr-win-cro-attack": 0.4,

    "fc-win-pac-attack": 0.5,
    "fc-win-tec-attack": 0.35,
    "fc-win-pos-attack": 0.5,
    "fc-win-hea-attack": 0.95,

    "fl-win-pac-attack": 0.5,
    "fl-win-tec-attack": 0.35,
    "fl-win-pas-attack": 0.4,
    "fl-win-cro-attack": 0.8,

    "fr-win-pac-attack": 0.5,
    "fr-win-tec-attack": 0.35,
    "fr-win-pas-attack": 0.4,
    "fr-win-cro-attack": 0.8,

    "dc-win-mar-defend": 0.5,
    "dc-win-tak-defend": 0.3,
    "dc-win-pos-defend": 0.5,
    "dc-win-hea-defend": 0.8,

    "dl-win-mar-defend": 0.5,
    "dl-win-tak-defend": 0.5,
    "dl-win-pos-defend": 0.5,
    "dl-win-hea-defend": 0.5,

    "dr-win-mar-defend": 0.5,
    "dr-win-tak-defend": 0.5,
    "dr-win-pos-defend": 0.5,
    "dr-win-hea-defend": 0.5,

    "mc-win-pac-defend": 0.5,
    "mc-win-mar-defend": 0.8,
    "mc-win-tak-defend": 0.65,

    "ml-win-pac-defend": 0.5,
    "ml-win-mar-defend": 0.8,
    "ml-win-tak-defend": 0.65,

    "mr-win-pac-defend": 0.5,
    "mr-win-mar-defend": 0.8,
    "mr-win-tak-defend": 0.65,

    "fc-win-pac-defend": 0.5,
    "fc-win-mar-defend": 0.8,
    "fc-win-tak-defend": 0.65,

    "fl-win-pac-defend": 0.5,
    "fl-win-mar-defend": 0.8,
    "fl-win-tak-defend": 0.65,

    "fr-win-pac-defend": 0.5,
    "fr-win-mar-defend": 0.8,
    "fr-win-tak-defend": 0.65,
}

OUTFIELDER_SKILLS = ["pac", "mar", "tak", "tec",
                     "pas", "pos", "cro", "hea", "fin", "lon"]
ZONES = ["dc", "dl", "dr", "mc", "ml", "mr", "fc", "fl", "fr"]
ZONE_TO_ATTACKER_POS_DICT = {
    "dc": ["dc", "dmc"],
    "dl": ["dl", "dml"],
    "dr": ["dr", "dmr"],
    "mc": ["mc", "dmc", "amc"],
    "ml": ["ml", "dml", "aml"],
    "mr": ["mr", "dmr", "amr"],
    "fc": ["fc", "amc"],
    "fl": ["fl", "aml"],
    "fr": ["fr", "amr"],
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
