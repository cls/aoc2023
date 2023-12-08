#!/usr/bin/env python3

import itertools
import re
import sys

network_pattern = re.compile(r'(?P<source>\w+) = \((?P<left>\w+), (?P<right>\w+)')

def parse_maps(lines):
    instructions = ''
    network = None
    for line in lines:
        if line == '\n':
            network = {}
        elif network is None:
            instructions += line.strip()
        else:
            match = network_pattern.match(line)
            source, left, right = match.group('source', 'left', 'right')
            network[source] = (left, right)
    return instructions, network

def follow_instructions(location, instructions, network):
    for instruction in itertools.cycle(instructions):
        left, right = network[location]
        location = {'L': left, 'R': right}[instruction]
        yield location

def steps_to_destination(source, destinations, instructions, network):
    for steps, location in enumerate(follow_instructions(source, instructions, network), 1):
        if location in destinations:
            return steps

if __name__ == '__main__':
    instructions, network = parse_maps(sys.stdin)
    print(steps_to_destination('AAA', {'ZZZ'}, instructions, network))
