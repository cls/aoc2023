#!/usr/bin/env python3

import re
import sys

pattern = re.compile(r'(?P<row>[.#?]+) (?P<damage>\d+(?:,\d+)*)')

def parse_records(line):
    match = pattern.match(line)
    row, damage_str = match.group('row', 'damage')
    damage = tuple(map(int, damage_str.split(',')))
    return row, damage

def possible_arrangements(record):
    row, damage = record
    state = (damage, '?')
    states = {state: 1}
    for spring in row:
        new_states = {}
        for (damage, expect), count in states.items():
            if spring != '#' and expect != '#':
                new_state = (damage, '?' if damage else '.')
                new_states[new_state] = new_states.get(new_state, 0) + count
            if spring != '.' and expect != '.':
                if damage[0] == 1:
                    new_state = (damage[1:], '.')
                else:
                    new_state = ((damage[0] - 1,) + damage[1:], '#')
                new_states[new_state] = new_states.get(new_state, 0) + count
        states = new_states
    end_state = ((), '.')
    count = states.get(end_state, 0)
    return count

if __name__ == '__main__':
    records = list(map(parse_records, sys.stdin))
    print(sum(map(possible_arrangements, records)))
