#!/usr/bin/env python3

from part1 import parse_cube_games

import sys

def minimal_cube_bag(game):
    bag = {}
    for cubes in game:
        for color, count in cubes.items():
            if bag.get(color, 0) < count:
                bag[color] = count
    return bag

def power_of_cube_set(cubes):
    return cubes.get('red', 0) * cubes.get('green', 0) * cubes.get('blue', 0)

if __name__ == '__main__':
    games = parse_cube_games(sys.stdin)
    print(sum(power_of_cube_set(minimal_cube_bag(game)) for game in games.values()))
