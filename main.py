from distutils.command.build_scripts import first_line_re
from parse_scorecard import parse_batting, parse_bowling
from tabulate import tabulate
import json
import argparse


def get_batting_performances(perf_info: dict[str, str]):
    ret = []

    for key, value in perf_info.items():
        parsed = parse_batting(value).as_array(key)
        ret.append(parsed)

    return ret


def get_bowling_performances(perf_info: dict[str, str]):
    ret = []

    for key, value in perf_info.items():
        parsed = parse_bowling(value).as_array(key)
        ret.append(parsed)

    return ret


def print_formatted_performances(batting_perfs, bowling_perfs):
    batting_columns = ["Name", "Runs", "Balls", "4s", "6s", "SR"]
    bowling_columns = ["Name", "Overs", "No Balls",
                       "Wides", "Runs", "Wickets", "Eco"]

    print("\nBatting\n")
    print(tabulate(batting_perfs, headers=batting_columns))
    print("-"*65)
    print("\nBowling\n")
    print(tabulate(bowling_perfs, headers=bowling_columns))
    print("-"*65)


def load_from_json(file_path):
    f = open(file_path)
    parsed = json.load(f)

    first_innings_batting = get_batting_performances(
        parsed['first_innings']['batting'])
    first_innings_bowling = get_bowling_performances(
        parsed['first_innings']['bowling'])
    second_innings_batting = get_batting_performances(
        parsed['second_innings']['batting'])
    second_innings_bowling = get_bowling_performances(
        parsed['second_innings']['bowling'])

    return (first_innings_batting, first_innings_bowling), (second_innings_batting, second_innings_bowling)


def main(path):
    first, second = load_from_json(path)

    print("First Innings: \n")
    print_formatted_performances(*first)
    print("\nSecond Innings: \n")
    print_formatted_performances(*second)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("path", help="Path to the scorecard file.")

    args = parser.parse_args()

    main(args.path)
