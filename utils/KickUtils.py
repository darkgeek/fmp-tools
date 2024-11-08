from model.Lineup import Lineup, LineupPlayer
from model.Player import Player
from model.KickingBattleReport import KickingBattleReport
from model.ScoreBattleReport import ScoreBattleReport
from model.KickStyle import KickStyle
from model.AttackingStyle import AttackingStyle
from utils.PlayerUtils import get_by_no, get_by_pos, get_by_pos_list

ACTION_TO_FINALIZATION_DICT = {
    AttackingStyle.FIL: {
        KickStyle.SHO: 0.45,
        KickStyle.LON: 0.2,
        KickStyle.HEA: 0.4,
        KickStyle.OVE: 0.025,
        KickStyle.LOB: 0.025,
    },
    AttackingStyle.SHO: {
        KickStyle.SHO: 0.65,
        KickStyle.LON: 0.10,
        KickStyle.HEA: 0.25,
        KickStyle.OVE: 0.01,
        KickStyle.LOB: 0.15,
    },
    AttackingStyle.LON: {
        KickStyle.SHO: 0.4,
        KickStyle.LON: 0.3,
        KickStyle.HEA: 0.4,
        KickStyle.OVE: 0.025,
        KickStyle.LOB: 0.025,
    },
    AttackingStyle.COU: {
        KickStyle.SHO: 0.2,
        KickStyle.LON: 0.4,
        KickStyle.HEA: 0.4,
        KickStyle.OVE: 0.01,
        KickStyle.LOB: 0.15,
    },
    AttackingStyle.WIN: {
        KickStyle.SHO: 0.4,
        KickStyle.LON: 0.2,
        KickStyle.HEA: 0.5,
        KickStyle.OVE: 0.15,
        KickStyle.LOB: 0.01,
    },
}

KICK_TO_SKILL_DICT = {
    KickStyle.SHO: {
        "attack": {
            "tak": 0.35,
            "tec": 0.35,
            "pos": 0.35,
        },
        "defend": {
            "mar": 0.35,
            "tak": 0.35,
            "tec": 0.15,
            "pos": 0.25,
        }
    },
    KickStyle.LON: {
        "attack": {
            "tak": 0.35,
            "tec": 0.35,
            "pos": 0.35,
        },
        "defend": {
            "mar": 0.35,
            "tak": 0.35,
            "tec": 0.15,
            "pos": 0.25,
        }
    },
    KickStyle.HEA: {
        "attack": {
            "tec": 0.2,
            "pos": 0.35,
            "hea": 0.55,
        },
        "defend": {
            "mar": 0.2,
            "tak": 0.1,
            "pos": 0.35,
            "hea": 0.55,
        }
    },
    KickStyle.OVE: {
        "attack": {
            "tec": 0.5,
            "pos": 0.4,
            "hea": 0.1
        },
        "defend": {
            "mar": 0.3,
            "tak": 0.3,
            "pos": 0.3,
        }
    },
    KickStyle.LOB: {
        "attack": {
            "tec": 0.6,
            "pos": 0.4,
        },
        "defend": {
            "mar": 0.3,
            "tak": 0.3,
            "pos": 0.3,
        }
    },
}

SCOREING_TYPE_TO_SKILLS_DICT = {
    KickStyle.SHO: {
        "attack": {
            "tec": 0.35,
            "pos": 0.35,
            "fin": 0.35,
        },
        "defend": {
            "han": 0.2,
            "one": 0.35,
            "ref": 0.35,
            "pos": 0.2,
        }
    },
    KickStyle.LON: {
        "attack": {
            "tec": 0.2,
            "pos": 0.2,
            "fin": 0.3,
            "lon": 0.35,
        },
        "defend": {
            "han": 0.3,
            "ref": 0.2,
            "aer": 0.2,
            "pos": 0.3,
            "jum": 0.2,
        }
    },
    KickStyle.HEA: {
        "attack": {
            "tec": 0.1,
            "pos": 0.35,
            "hea": 0.35,
            "pos": 0.2,
        },
        "defend": {
            "han": 0.3,
            "ref": 0.15,
            "aer": 0.2,
            "pos": 0.15,
            "jum": 0.15,
            "ele": 0.15,
        }
    },
    KickStyle.OVE: {
        "attack": {
            "tec": 0.55,
            "pos": 0.3,
            "fin": 0.3,
        },
        "defend": {
            "han": 0.3,
            "ref": 0.2,
            "aer": 0.2,
            "pos": 0.3,
            "jum": 0.2,
        }
    },
    KickStyle.LOB: {
        "attack": {
            "tec": 0.5,
            "pos": 0.1,
            "fin": 0.35,
        },
        "defend": {
            "han": 0.2,
            "ref": 0.25,
            "aer": 0.2,
            "pos": 0.15,
            "jum": 0.15,
            "ele": 0.25,
        }
    },
}

KICK_PLAYER_POSITIONS = ["fc", "amc", "aml", "amr"]
DEFEND_PLAYER_POSITIONS = ["dc", "dl", "dr", "dmc"]


def buildBattleReport(attackers: [LineupPlayer], defenders: [LineupPlayer], allAttackers: [Player], allDefenders: [Player]) -> {}:
    styleToReportsDict = {}

    aPlayers = get_by_pos_list(KICK_PLAYER_POSITIONS, attackers)
    dPlayers = get_by_pos_list(DEFEND_PLAYER_POSITIONS, defenders)
    gkPlayer = get_by_pos("gk", defenders)[0]
    fullGkPlayer = get_by_no(gkPlayer.no, allDefenders)

    for aStyle in AttackingStyle:
        reports = []
        for ap in aPlayers:
            fullAp = get_by_no(ap.no, allAttackers)
            for dp in dPlayers:
                fullDp = get_by_no(dp.no, allDefenders)
                reports.append(buildOneOnOneBattleReport(
                    fullAp, ap.position, fullDp, dp.position, aStyle, fullGkPlayer))

        styleToReportsDict[aStyle] = reports

    return reports


def buildOneOnOneBattleReport(attacker: Player, aPos: str, defender: Player, dPos: str, aStyle: AttackingStyle, gk: Player) -> KickingBattleReport:

    duelData = []
    kickStyleToPosibilityDict = ACTION_TO_FINALIZATION_DICT.get(aStyle, {})
    for kickStyle in kickStyleToPosibilityDict.keys():
        kickStyleToWinPossibilityDict = {}
        aGrade = 0
        dGrade = 0

        directionToSkillsDict = KICK_TO_SKILL_DICT.get(kickStyle, {})

        aSkillsDict = directionToSkillsDict.get("attack", {})
        for sk in aSkillsDict.keys():
            aGrade = aGrade + aSkillsDict.get(sk, 0) * getattr(attacker, sk)

        dSkillsDict = directionToSkillsDict.get("defend", {})
        for sk in dSkillsDict.keys():
            dGrade = dGrade + dSkillsDict.get(sk, 0) * getattr(defender, sk)

        scoreReport = buildScoreReport(attacker, gk, kickStyle)
        kickStyleToWinPossibilityDict["kickStyle"] = kickStyle
        kickStyleToWinPossibilityDict["duelWin"] = aGrade / (aGrade + dGrade)
        kickStyleToWinPossibilityDict["scoreWin"] = scoreReport.score_method_grade / (
            scoreReport.score_method_grade + scoreReport.gk_tactic_grade)
        kickStyleToWinPossibilityDict["frequency"] = kickStyleToPosibilityDict.get(
            kickStyle, 0)
        duelData.append(kickStyleToWinPossibilityDict)

    return KickingBattleReport(attacker=attacker.name, attacker_pos=aPos, attacker_energy=attacker.form, attacker_overall_grade=attacker.rating, defender=defender.name, defender_pos=dPos, defender_energy=defender.form, defender_overall_grade=defender.rating, gk_energy=scoreReport.gk_energy, gk_overall_grade=scoreReport.gk_overall_grade, duel_win_possibilities=duelData)


def buildScoreReport(attacker: Player, gk: Player, kStyle: KickStyle) -> ScoreBattleReport:
    aGrade = 0
    dGrade = 0

    directionToSkillsDict = SCOREING_TYPE_TO_SKILLS_DICT.get(kStyle, {})
    aSkillsDict = directionToSkillsDict.get("attack", {})
    for sk in aSkillsDict.keys():
        aGrade = aGrade + aSkillsDict.get(sk, 0) * getattr(attacker, sk)

    dSkillsDict = directionToSkillsDict.get("defend", {})
    for sk in dSkillsDict.keys():
        dGrade = dGrade + dSkillsDict.get(sk, 0) * getattr(gk, sk)

    return ScoreBattleReport(score_method_grade=aGrade, gk_energy=gk.form, gk_overall_grade=gk.rating, gk_tactic_grade=dGrade)
