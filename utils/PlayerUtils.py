from model.Player import Player


def get_by_no(no: int, players: [Player]) -> Player:
    for p in players:
        if p.no == no:
            return p

    return None


def get_by_pos(pos: str, players: [Player]) -> [Player]:
    players = []

    for p in players:
        if p.pos == pos:
            players.append(p)

    return players
