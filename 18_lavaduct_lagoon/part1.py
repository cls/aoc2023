#!/usr/bin/env python3

import re
import sys

directions = {
    'U': (0, -1),
    'D': (0, +1),
    'L': (-1, 0),
    'R': (+1, 0),
}

dig_pattern = re.compile(r'(?P<direction>[UDLR]) (?P<distance>\d+) \(#(?P<color>[0-9a-f]{6})\)\n?')

def parse_dig_plan(lines):
    for line in lines:
        match = dig_pattern.fullmatch(line)
        direction_str, distance_str, color_str = match.group('direction', 'distance', 'color')
        yield directions[direction_str], int(distance_str)

def dig_trench(plan):
    x, y = 0, 0
    for direction, distance in plan:
        yield x, y
        xd, yd = direction
        x += xd * distance
        y += yd * distance

def polygon_area(corners):
    area = 0
    n = len(corners)
    for i in range(n):
        j = (i + 1) % n
        x1, y1 = corners[i]
        x2, y2 = corners[j]
        area += x1 * y2
        area -= x2 * y1
    return abs(area) // 2

def trench_volume(plan):
    trench = list(dig_trench(plan))
    length = sum(distance for direction, distance in plan) // 2
    return polygon_area(trench) + length + 1

if __name__ == '__main__':
    dig_plan = list(parse_dig_plan(sys.stdin))
    print(trench_volume(dig_plan))
