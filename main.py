import argparse
import pprint

from utils.DataLoaders import load_players, load_lineup_data
from model.Lineup import Lineup, LineupPlayer
from model.AttackingStyle import AttackingStyle
from model.KickStyle import KickStyle
from model.ClashReport import ClashReport
from utils.ClashUtils import buildClashReport
from utils.KickUtils import buildBattleReport

print("Loading my players...")
my_players = load_players("my_players.json")
print("Done.")

print("Loading opponent players...")
opponent_players = load_players("opponent_players.json")
print("Done.")

print("Loading my lineup...")
my_lineup = load_lineup_data("my_lineup.data")
print("Done.")

print("Loading opponent lineup...")
opponent_lineup = load_lineup_data("opponent_lineup.data")
print("Done.")

attack_reports = buildClashReport(
    my_lineup.players, opponent_lineup.players, AttackingStyle.FIL, my_players, opponent_players)
print("=======Attacking Report=======")
pprint.pp(attack_reports)

print("\n\n")

print("=======Defending Report=======")
defend_reports = buildClashReport(
    opponent_lineup.players, my_lineup.players, AttackingStyle.FIL, opponent_players, my_players)
pprint.pp(defend_reports)

print("\n\n")

print("=======Attacking Kicking Report=======")
attack_kick_reports = buildBattleReport(
    my_lineup.players, opponent_lineup.players, AttackingStyle.FIL, my_players, opponent_players)
pprint.pp(attack_kick_reports)

print("\n\n")

print("=======Defending Kicking Report=======")
defend_kick_reports = buildBattleReport(
    opponent_lineup.players, my_lineup.players, AttackingStyle.FIL, opponent_players, my_players)
pprint.pp(defend_kick_reports)
