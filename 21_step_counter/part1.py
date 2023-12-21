#!/usr/bin/env python3

import sys

def parse_garden(lines):
    start = None
    plots = set()
    for y, line in enumerate(lines):
        for x, feature in enumerate(line.strip()):
            location = (x, y)
            if feature == 'S':
                start = location
            if feature != '#':
                plots.add(location)
    return start, plots

def reachable_plots(start, plots, steps):
    reach = {start}
    for step in range(steps):
        reach_next = set()
        for x, y in reach:
            if (x, y-1) in plots:
                reach_next.add((x, y-1))
            if (x+1, y) in plots:
                reach_next.add((x+1, y))
            if (x, y+1) in plots:
                reach_next.add((x, y+1))
            if (x-1, y) in plots:
                reach_next.add((x-1, y))
        reach = reach_next
    return reach

if __name__ == '__main__':
    start, plots = parse_garden(sys.stdin)
    print(len(reachable_plots(start, plots, 64)))
