#!/usr/bin/env python3

from part1 import find_galaxies, expand_cosmos, distances_between_galaxies

import sys

if __name__ == '__main__':
    image = list(line.strip() for line in sys.stdin)
    galaxies = set(find_galaxies(image))
    expanded_galaxies = set(expand_cosmos(galaxies, 1000000))
    print(sum(distances_between_galaxies(expanded_galaxies)))
