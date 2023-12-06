#!/usr/bin/env python3

from part1 import number_of_ways_to_win

import sys

def parse_race(lines):
    race = {}
    for line in lines:
        key, value_str = line.split(':')
        value = int(value_str.replace(' ', ''))
        race[key] = value
    return race

if __name__ == '__main__':
    race = parse_race(sys.stdin)
    print(number_of_ways_to_win(race))
