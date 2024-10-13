import argparse

from utils.DataLoaders import load_players, load_lineup_data
from model.Lineup import Lineup, LineupPlayer
from model.AttackingStyle import AttackingStyle
from model.KickStyle import KickStyle
from model.ClashReport import ClashReport
from utils.PlayerUtils import get_by_no, get_by_pos

my_players = load_players("my_players.json")
print(my_players)

opponent_players = load_players("opponent_players.json")
print(opponent_players)

my_lineup = load_lineup_data("my_lineup.data")
print(my_lineup)

opponent_lineup = load_lineup_data("opponent_lineup.data")
print(opponent_lineup)
