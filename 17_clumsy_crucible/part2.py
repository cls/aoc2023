#!/usr/bin/env python3

from part1 import State, parse_city, find_crucible_path

import sys

if __name__ == '__main__':
    city = parse_city(sys.stdin)
    print(find_crucible_path(city, max_speed=10, min_turn_speed=4))
