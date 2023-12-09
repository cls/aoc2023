#!/usr/bin/env python3

import itertools
import sys

def extrapolate_next_value(values):
    if not any(values):
        return 0
    deltas = list(b - a for a, b in itertools.pairwise(values))
    next_value = values[-1] + extrapolate_next_value(deltas)
    return next_value

if __name__ == '__main__':
    values = (list(map(int, line.split())) for line in sys.stdin)
    print(sum(map(extrapolate_next_value, values)))
