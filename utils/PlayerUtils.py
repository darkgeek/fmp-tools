from model.Player import Player
from model.Lineup import Lineup, LineupPlayer


def get_by_no(no: int, players: [Player]) -> Player:
    for p in players:
        if p.no == no:
            return p

    return None


def get_by_pos(pos: str, players: [LineupPlayer]) -> LineupPlayer:
    for p in players:
        if p.position == pos:
            return p

    return None


def get_by_pos_list(posList: [str], players: [LineupPlayer]) -> [LineupPlayer]:
    candidates = []

    for pos in posList:
        player = get_by_pos(pos, players)

        if player is None:
            continue

        candidates.append(player)

    return candidates
