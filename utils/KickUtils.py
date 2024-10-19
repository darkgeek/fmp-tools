from model.Lineup import Lineup, LineupPlayer
from model.Player import Player
from model.KickingBattleReport import KickingBattleReport
from model.ScoreBattleReport import ScoreBattleReport
from model.KickStyle import KickStyle
from model.AttackingStyle import AttackingStyle
from utils.PlayerUtils import get_by_no, get_by_pos, get_by_pos_list

ACTION_TO_FINALIZATION_DICT = {
    AttackingStyle.FIL: {
        KickStyle.SHO: 0.4,
        KickStyle.LON: 0.2,
        KickStyle.HEA: 0.35,
        KickStyle.OVE: 0.025,
        KickStyle.LOB: 0.025,
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
    }
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
    }
}

KICK_PLAYER_POSITIONS = ["fc", "amc", "aml", "amr"]
DEFEND_PLAYER_POSITIONS = ["dc", "dl", "dr", "dmc"]


def buildBattleReport(attackers: [LineupPlayer], defenders: [LineupPlayer], style: AttackingStyle, allAttackers: [Player], allDefenders: [Player]) -> [KickingBattleReport]:
    reports = []

    aPlayers = get_by_pos_list(KICK_PLAYER_POSITIONS, attackers)
    dPlayers = get_by_pos_list(DEFEND_PLAYER_POSITIONS, defenders)
    gkPlayer = get_by_pos("gk", defenders)
    fullGkPlayer = get_by_no(gkPlayer.no, allDefenders)

    for ap in aPlayers:
        fullAp = get_by_no(ap.no, allAttackers)
        for dp in dPlayers:
            fullDp = get_by_no(dp.no, allDefenders)
            reports.extend(buildOneOnOneBattleReport(
                fullAp, ap.position, fullDp, dp.position, style, fullGkPlayer))

    return reports


def buildOneOnOneBattleReport(attacker: Player, aPos: str, defender: Player, dPos: str, aStyle: AttackingStyle, gk: Player) -> [KickingBattleReport]:
    reports = []

    kickStyleToPosibilityDict = ACTION_TO_FINALIZATION_DICT.get(aStyle, {})
    for kickStyle in kickStyleToPosibilityDict.keys():
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

        report = KickingBattleReport(style=kickStyle, possibility=kickStyleToPosibilityDict.get(kickStyle, 0), attacker=attacker.name, attacker_pos=aPos, attacker_energy=attacker.form, attacker_overall_grade=attacker.rating,
                                     attacker_tactic_grade=aGrade, defender=defender.name, defender_pos=dPos, defender_energy=defender.form, defender_overall_grade=defender.rating, defender_tactic_grade=dGrade, score_method_grade=scoreReport.score_method_grade, gk_energy=scoreReport.gk_energy, gk_overall_grade=scoreReport.gk_overall_grade, gk_tactic_grade=scoreReport.gk_tactic_grade)
        reports.append(report)

    return reports


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
