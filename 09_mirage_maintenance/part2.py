#!/usr/bin/env python3

import itertools
import sys

def extrapolate_prev_value(values):
    if not any(values):
        return 0
    deltas = list(b - a for a, b in itertools.pairwise(values))
    prev_value = values[0] - extrapolate_prev_value(deltas)
    return prev_value

if __name__ == '__main__':
    values = (list(map(int, line.split())) for line in sys.stdin)
    print(sum(map(extrapolate_prev_value, values)))
