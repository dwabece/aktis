#!/usr/bin/env python
import statistics as statistics
from argparse import ArgumentParser
import utils

parser = ArgumentParser()
parser.add_argument(
    '-i', '--inputfile', dest='filename',
    required=True,
    help='Fixture to be loaded and processed.')


if __name__ == '__main__':
    args = parser.parse_args()

    data = utils.load_input(args.filename, input_type='median')
    intdata = [int(i) for i in data.splitlines()][1:]

    res = []
    for i in intdata:
        res.append(i)
        listmed = float(statistics.median(res))
        print(listmed)
