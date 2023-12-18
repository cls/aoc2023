#!/usr/bin/env python3

from part1 import dig_pattern, directions, trench_volume

import sys

def parse_real_dig_plan(lines):
    for line in lines:
        match = dig_pattern.fullmatch(line)
        direction_str, distance_str, color_str = match.group('direction', 'distance', 'color')
        real_direction_str = 'RDLU'[int(color_str[-1], base=0x10)]
        real_distance = int(color_str[:-1], base=0x10)
        yield directions[real_direction_str], real_distance

if __name__ == '__main__':
    dig_plan = list(parse_real_dig_plan(sys.stdin))
    print(trench_volume(dig_plan))
