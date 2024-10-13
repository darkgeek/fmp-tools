from utils.FileUtils import readFileAsJson, readFileByLines
from model.Player import Player
from model.Lineup import Lineup, LineupPlayer


def load_players(players_data_file: str) -> []:
    players_raw_data = readFileAsJson(players_data_file)

    players = []
    for player_id in players_raw_data.keys():
        player_raw = players_raw_data[player_id]
        sk = player_raw["sk"]
        player = Player(no=int(player_raw["no"]),
                        name=player_raw["name"],
                        rating=player_raw["rating"],
                        form=sk["For"],
                        routine=sk["Rou"],

                        mar=sk.get("Mar", None),
                        tak=sk.get("Tak", None),
                        tec=sk.get("Tec", None),
                        pas=sk.get("Pas", None),
                        cro=sk.get("Cro", None),
                        fin=sk.get("Fin", None),
                        hea=sk.get("Hea", None),
                        lon=sk.get("Lon", None),
                        pos=sk.get("Pos", None),
                        sta=sk.get("Sta", None),
                        pac=sk.get("Pac", None),

                        han=sk.get("Han", None),
                        one=sk.get("One", None),
                        ref=sk.get("Ref", None),
                        aer=sk.get("Aer", None),
                        ele=sk.get("Ele", None),
                        jum=sk.get("Jum", None),
                        kic=sk.get("Kic", None),
                        thr=sk.get("Thr", None))
        players.append(player)

    return players


def load_lineup_data(lineup_data_file: str) -> Lineup:
    lineup_raw_data = readFileByLines(lineup_data_file)

    players = []
    for line in lineup_raw_data:
        line = line.replace("\n", "")
        parts = line.split()
        player = LineupPlayer(no=int(parts[1]), position=parts[0])
        players.append(player)

    return Lineup(players=players)
