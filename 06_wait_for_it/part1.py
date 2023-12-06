#!/usr/bin/env python3

import math
import sys

def parse_races(lines):
    races = []
    for line in lines:
        key, values_str = line.split(':')
        values = list(map(int, values_str.split()))
        for index, value in enumerate(values):
            if index == len(races):
                races.append({})
            races[index][key] = value
    return races

def solve_quadratic(a, b, c):
    d = math.sqrt((b ** 2) - (4 * a * c))
    root1 = (-b - d) / (2 * a)
    root2 = (-b + d) / (2 * a)
    return root1, root2

def number_of_ways_to_win(race):
    time = race['Time']
    distance = race['Distance']
    min_root, max_root = solve_quadratic(1, -time, distance + 1)
    min_hold = math.ceil(min_root)
    max_hold = math.floor(max_root)
    return max_hold - min_hold + 1

if __name__ == '__main__':
    races = parse_races(sys.stdin)
    print(math.prod(map(number_of_ways_to_win, races)))
