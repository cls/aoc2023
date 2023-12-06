#!/usr/bin/env python3

import math
import sys

def parse_races(lines):
    races = []
    for line in lines:
        key, values_str = line.split(':')
        values = list(map(int, values_str.split()))
        for index, value in enumerate(values):
            if index == len(races):
                races.append({})
            races[index][key] = value
    return races

def ways_to_win(race):
    time = race['Time']
    distance = race['Distance']
    for hold_time in range(time):
        move_time = time - hold_time
        if hold_time * move_time > distance:
            yield hold_time

def number_of_ways_to_win(race):
    return sum(1 for hold_time in ways_to_win(race))

if __name__ == '__main__':
    races = parse_races(sys.stdin)
    print(math.prod(map(number_of_ways_to_win, races)))
