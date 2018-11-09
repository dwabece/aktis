#!/usr/bin/env python
from argparse import ArgumentParser
import utils

parser = ArgumentParser()
parser.add_argument(
    '-i', '--inputfile', dest='filename',
    required=True,
    help='Fixture to be loaded and processed.')


def middle_row_med(inp):
    lenx = len(inp)
    iseven = lenx % 2 == 0
    mid = lenx // 2

    if iseven:
        return (inp[mid - 1] + inp[mid]) / 2
    return inp[mid]


if __name__ == '__main__':
    args = parser.parse_args()

    data = utils.load_input(args.filename, input_type='median')
    intdata = [int(i) for i in data.splitlines()][1:]

    res = []
    for i in intdata:
        res.append(i)
        res.sort()
        print(float(middle_row_med(res)))
