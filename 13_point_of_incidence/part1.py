#!/usr/bin/env python3

import sys

def parse_terrain(lines):
    terrain = []
    for line in map(str.strip, lines):
        if line:
            terrain.append(line)
        else:
            yield terrain
            terrain = []
    if terrain:
        yield terrain

def find_mirrors(terrain):
    for x in range(1, len(terrain[0])):
        depth = min(x, len(terrain[0])-x)
        original = [row[x-depth:x][::-1] for row in terrain]
        reflection = [row[x:x+depth] for row in terrain]
        if original == reflection:
            yield x
    for y in range(1, len(terrain)):
        depth = min(y, len(terrain)-y)
        original = terrain[y-depth:y][::-1]
        reflection = terrain[y:y+depth]
        if original == reflection:
            yield y * 100

def find_mirror(terrain):
    return next(find_mirrors(terrain))

if __name__ == '__main__':
    terrains = list(parse_terrain(sys.stdin))
    print(sum(map(find_mirror, terrains)))
