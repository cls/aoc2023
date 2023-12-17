#!/usr/bin/env python3

from collections import namedtuple

import heapq
import sys

State = namedtuple('State', ['location', 'direction', 'speed'])

def parse_city(lines):
    city = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            city[(x, y)] = int(char)
    return city

def find_crucible_path(city, max_speed, min_turn_speed=0):
    start_state = State(location=(0, 0), direction=(0, 0), speed=0)
    end_location = max(city.keys())
    heap = []
    heapq.heappush(heap, (0, start_state))
    heat_loss_by_state = {start_state: 0}
    while heap:
        heat_loss, state = heapq.heappop(heap)
        if state.location == end_location and state.speed >= min_turn_speed:
            return heat_loss
        for next_state in next_crucible_states(state, max_speed, min_turn_speed):
            if next_state.location in city:
                next_heat_loss = heat_loss + city[next_state.location]
                if next_state not in heat_loss_by_state or next_heat_loss < heat_loss_by_state[next_state]:
                    heat_loss_by_state[next_state] = next_heat_loss
                    heapq.heappush(heap, (next_heat_loss, next_state))

def next_crucible_states(state, max_speed, min_turn_speed):
    x, y = state.location
    for direction in next_directions(state.direction):
        xd, yd = direction
        location = (x+xd, y+yd)
        turning = state.direction != (0, 0) and direction != state.direction
        if state.speed >= min_turn_speed if turning else state.speed < max_speed:
            speed = 1 if turning else state.speed + 1
            yield State(location=location, direction=direction, speed=speed)

def next_directions(direction):
    if direction == (0, 0):
        yield 0, -1
        yield +1, 0
        yield 0, +1
        yield -1, 0
    else:
        xd, yd = direction
        yield xd, yd
        yield yd, xd
        yield -yd, -xd

if __name__ == '__main__':
    city = parse_city(sys.stdin)
    print(find_crucible_path(city, max_speed=3))
