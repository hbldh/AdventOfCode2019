#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import importlib
from AOC2019 import run_solver

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
        except:
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
