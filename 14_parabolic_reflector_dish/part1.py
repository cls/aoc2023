#!/usr/bin/env python3

import sys

def tilt_north(platform):
    north = [0] * len(platform[0])
    for y, row in enumerate(platform):
        for x, cell in enumerate(row):
            if cell == 'O':
                if north[x] != y:
                    platform[y][x] = '.';
                    platform[north[x]][x] = 'O';
                north[x] += 1
            elif cell == '#':
                north[x] = y + 1

def calculate_load(platform):
    for y, row in enumerate(platform):
        for cell in row:
            if cell == 'O':
                yield len(platform) - y

if __name__ == '__main__':
    platform = [list(line.strip()) for line in sys.stdin]
    tilt_north(platform)
    print(sum(calculate_load(platform)))
