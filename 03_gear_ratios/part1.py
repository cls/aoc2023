#!/usr/bin/env python3

import re
import sys

number_pattern = re.compile(r'\d+')
part_pattern = re.compile(r'[^.\d\n]')

def find_parts(schematic, start, end, pos, endpos):
    for index in range(max(0, start), min(end, len(schematic))):
        line = schematic[index]
        for match in part_pattern.finditer(line, max(0, pos), min(endpos, len(line))):
            location = (index, match.start())
            part = match.group()
            yield location, part

def find_numbered_parts(schematic):
    for index, line in enumerate(schematic):
        for match in number_pattern.finditer(line):
            number = int(match.group())
            pos, endpos = match.span()
            for location, part in find_parts(schematic, index - 1, index + 2, pos - 1, endpos + 1):
                yield location, part, number

def find_part_numbers(schematic):
    for location, part, number in find_numbered_parts(schematic):
        yield number

if __name__ == '__main__':
    schematic = list(sys.stdin)
    print(sum(find_part_numbers(schematic)))
