#!/usr/bin/env python3

from part1 import parse_terrain, find_mirror, find_mirrors

import sys

def find_smudged_mirror(terrain):
    terrain = list(map(list, terrain))
    unsmudged_mirror = find_mirror(terrain)
    for y, row in enumerate(terrain):
        for x, cell in enumerate(row):
            row[x] = '.' if cell == '#' else '#'
            for mirror in find_mirrors(terrain):
                if mirror != unsmudged_mirror:
                    return mirror
            row[x] = cell

if __name__ == '__main__':
    terrains = list(parse_terrain(sys.stdin))
    print(sum(map(find_smudged_mirror, terrains)))
