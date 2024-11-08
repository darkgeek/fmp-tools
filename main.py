import argparse
import pprint

from utils.DataLoaders import load_players, load_lineup_data
from model.Lineup import Lineup, LineupPlayer
from model.AttackingStyle import AttackingStyle
from model.KickStyle import KickStyle
from model.ClashReport import ClashReport
from utils.ClashUtils import buildClashReport
from utils.KickUtils import buildBattleReport

# Instantiate the parser
parser = argparse.ArgumentParser(description='Trophymanager tactic helper')

parser.add_argument(
    '--mp', type=str, help='my players detail json file', required=True)
parser.add_argument(
    '--op', type=str, help='opponent players detail json file', required=True)
parser.add_argument(
    '--ml', type=str, help='my lineup data file', required=True)
parser.add_argument(
    '--ol', type=str, help='opponent lineup json file', required=True)

args = parser.parse_args()

# Load data
print("Loading my players...")
my_players = load_players(args.mp)
print("Done.")

print("Loading opponent players...")
opponent_players = load_players(args.op)
print("Done.")

print("Loading my lineup...")
my_lineup = load_lineup_data(args.ml)
print("Done.")

print("Loading opponent lineup...")
opponent_lineup = load_lineup_data(args.ol)
print("Done.")

# Build reports
attack_reports = buildClashReport(
    my_lineup.players, opponent_lineup.players, my_players, opponent_players)
print("=======Attacking Report=======")
pprint.pp(attack_reports)

print("\n\n")

print("=======Defending Report=======")
defend_reports = buildClashReport(
    opponent_lineup.players, my_lineup.players, opponent_players, my_players)
pprint.pp(defend_reports)

print("\n\n")

print("=======Attacking Kicking Report=======")
attack_kick_reports = buildBattleReport(
    my_lineup.players, opponent_lineup.players, my_players, opponent_players)
pprint.pp(attack_kick_reports)

print("\n\n")

print("=======Defending Kicking Report=======")
defend_kick_reports = buildBattleReport(
    opponent_lineup.players, my_lineup.players, opponent_players, my_players)
pprint.pp(defend_kick_reports)
