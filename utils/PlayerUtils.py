from model.Player import Player
from model.Lineup import Lineup, LineupPlayer


def get_by_no(no: int, players: [Player]) -> Player:
    for p in players:
        if p.no == no:
            return p

    return None


def get_by_pos(pos: str, players: [LineupPlayer]) -> [LineupPlayer]:
    candidates = []

    for p in players:
        if p.position == pos:
            candidates.append(p)

    return candidates


def get_by_pos_list(posList: [str], players: [LineupPlayer]) -> [LineupPlayer]:
    candidates = []

    for pos in posList:
        pos_players = get_by_pos(pos, players)

        for pp in pos_players:
            if pp in candidates:
                continue

            candidates.append(pp)

    return candidates
