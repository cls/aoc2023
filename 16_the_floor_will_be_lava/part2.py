#!/usr/bin/env python3

from part1 import N, E, S, W, energized_tiles

import sys

def beam_configurations(cave):
    for x, cell in enumerate(cave[0]):
        yield (x, -1), S
        yield (x, len(cave)), N
    for y, row in enumerate(cave):
        yield (-1, y), E
        yield (len(row), y), W

def optimal_beam_configuration(cave):
    return max(energized_tiles(cave, location, direction) for location, direction in beam_configurations(cave))

if __name__ == '__main__':
    cave = list(map(str.strip, sys.stdin))
    print(optimal_beam_configuration(cave))
