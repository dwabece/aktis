#!/usr/bin/env python
import statistics as statistics
from os import path as ospath
import config


def load_input(fname):
    fpath = ospath.join(config.MEDIAN_DIR, fname)
    try:
        with open(fpath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        pass


if __name__ == '__main__':
    data = load_input('input01.txt')
    intdata = [int(i) for i in data.splitlines()][1:]

    res = []
    for i in intdata:
        res.append(i)
        listmed = float(statistics.median(res))
        print(listmed)
