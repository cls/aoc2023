#!/usr/bin/env python3

from part1 import find_numbered_parts

import sys

def find_gear_ratios(schematic):
    gears = {}
    for location, part, number in find_numbered_parts(schematic):
        if part == '*':
            gears.setdefault(location, []).append(number)
    for numbers in gears.values():
        if len(numbers) == 2:
            ratio = numbers[0] * numbers[1]
            yield ratio

if __name__ == '__main__':
    schematic = list(sys.stdin)
    print(sum(find_gear_ratios(schematic)))
