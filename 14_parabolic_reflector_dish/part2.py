#!/usr/bin/env python3

from part1 import tilt_north, calculate_load

import sys

def tilt_west(platform):
    west = [0] * len(platform)
    for y, row in enumerate(platform):
        for x, cell in enumerate(row):
            if cell == 'O':
                if west[y] != x:
                    platform[y][x] = '.';
                    platform[y][west[y]] = 'O';
                west[y] += 1
            elif cell == '#':
                west[y] = x + 1

def tilt_south(platform):
    south = [len(platform)-1] * len(platform[0])
    for i, row in enumerate(platform[::-1]):
        y = len(platform) - i - 1
        for x, cell in enumerate(row):
            if cell == 'O':
                if south[x] != y:
                    platform[y][x] = '.';
                    platform[south[x]][x] = 'O';
                south[x] -= 1
            elif cell == '#':
                south[x] = y - 1

def tilt_east(platform):
    east = [len(platform[0])-1] * len(platform)
    for y, row in enumerate(platform):
        for i, cell in enumerate(row[::-1]):
            x = len(row) - i - 1
            if cell == 'O':
                if east[y] != x:
                    platform[y][x] = '.';
                    platform[y][east[y]] = 'O';
                east[y] -= 1
            elif cell == '#':
                east[y] = x - 1

def load_after_spin_cycles(platform, cycles):
    arrangements = {}
    loads = []
    for cycle in range(cycles):
        arrangement = tuple(map(str, platform))
        if arrangement in arrangements:
            first = arrangements[arrangement]
            period = cycle - first
            modulo = (cycles - first) % period
            index = first + modulo
            return loads[index]
        arrangements[arrangement] = cycle
        loads.append(sum(calculate_load(platform)))
        tilt_north(platform)
        tilt_west(platform)
        tilt_south(platform)
        tilt_east(platform)
    return loads[-1]

if __name__ == '__main__':
    platform = [list(line.strip()) for line in sys.stdin]
    print(load_after_spin_cycles(platform, 1000000000))
