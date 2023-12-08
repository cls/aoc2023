#!/usr/bin/env python3

from part1 import parse_maps, steps_to_destination

import functools
import math
import sys

def ghost_steps_to_destinations(sources, destinations, instructions, network):
    # TODO: This makes several assumptions about the input which may not hold in general.
    ghost_steps = {source: steps_to_destination(source, destinations, instructions, network) for source in sources}
    steps = functools.reduce(math.lcm, ghost_steps.values())
    return steps

if __name__ == '__main__':
    instructions, network = parse_maps(sys.stdin)
    sources = set(filter(lambda location: location.endswith('A'), network.keys()))
    destinations = set(filter(lambda location: location.endswith('Z'), network.keys()))
    print(ghost_steps_to_destinations(sources, destinations, instructions, network))
