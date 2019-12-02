#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import importlib
# from AOC2019 import run_solver

import os
from urllib.request import build_opener

root_dir = os.path.dirname(os.path.abspath(__file__))
import traceback

def ensure_data(day):
    day_input_file = os.path.join(root_dir, f'input_{day:02d}.txt')
    if not os.path.exists(day_input_file):
        session_token = os.environ.get('AOC_SESSION_TOKEN')
        if session_token is None:
            raise ValueError("Must set AOC_SESSION_TOKEN environment variable!")
        url = f'https://adventofcode.com/2019/day/{day}/input'
        opener = build_opener()
        opener.addheaders.append(('Cookie', f'session={session_token}'))
        response = opener.open(url)
        with open(day_input_file, 'w') as f:
            f.write(response.read().decode("utf-8"))


def load_data(day):
    with open(f'input_{day:02d}.txt', 'r') as f:
        data = f.read().strip()
    return data


def run_solver(f, file):
    day = int(file.split('/')[-1].strip('day').strip('.py'))
    ensure_data(day)
    data = load_data(day)

    part_1, part_2 = f(data)

    print("Part 1: {0}".format(part_1))
    print("Part 2: {0}".format(part_2))

def main(which_days):
    for day in which_days:
        try:
            day_module = importlib.import_module(
                'day{0:02d}'.format(day), '.')
        except:
            continue

        try:
            print("Solutions to Day {0:02d}\n-------------------".format(day))
            run_solver(day_module.solve, 'day{0:02d}'.format(day))
            print('')
        except Exception:
            traceback.print_exc()
            print("Day {0:02d} failed to run!\n".format(day))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser("Advent of Code AOC2019")
    parser.add_argument(
        'day', nargs='*', default=None, help="Run only specific day's problem")
    parser.add_argument(
        '--token', type=str, default=None,
        help="AoC session token. Needed to download data automatically.")
    args = parser.parse_args()

    if args.token:
        os.environ["AOC_SESSION_TOKEN"] = args.token

    if args.day:
        days = map(int, args.day)
    else:
        days = range(1, 26)

    main(days)
