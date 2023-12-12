#!/usr/bin/env python3

from part1 import parse_records, possible_arrangements

import sys

def unfold_record(record, copies=5):
    row, damage = record
    new_row = '?'.join(row for copy in range(copies))
    new_damage = damage * copies
    return new_row, new_damage

if __name__ == '__main__':
    records = list(map(parse_records, sys.stdin))
    unfolded_records = list(map(unfold_record, records))
    print(sum(map(possible_arrangements, unfolded_records)))
