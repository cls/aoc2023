#!/usr/bin/env python3

import sys

N = ( 0, -1)
E = (+1,  0)
S = ( 0, +1)
W = (-1,  0)

new_directions_by_tile = {
    '.':  {N: {N},    E: {E},    S: {S},    W: {W}},
    '/':  {N: {E},    E: {N},    S: {W},    W: {S}},
    '\\': {N: {W},    E: {S},    S: {E},    W: {N}},
    '|':  {N: {N},    E: {N, S}, S: {S},    W: {N, S}},
    '-':  {N: {E, W}, E: {E},    S: {E, W}, W: {W}},
}

def energized_tiles(cave, beam_location, beam_direction):
    beams = {beam_location: {beam_direction}}
    energized = {}
    while beams:
        location, directions = beams.popitem()
        x, y = location
        for direction in directions:
            xd, yd = direction
            new_location = (x+xd, y+yd)
            new_x, new_y = new_location
            if new_y < 0 or new_y >= len(cave) or new_x < 0 or new_x >= len(cave[new_y]):
                continue
            tile = cave[new_y][new_x]
            energized_directions = energized.setdefault(new_location, set())
            new_directions = new_directions_by_tile[tile][direction] - energized_directions
            if new_directions:
                beam_directions = beams.setdefault(new_location, set())
                beam_directions.update(new_directions)
                energized_directions.update(new_directions)
    return len(energized)

if __name__ == '__main__':
    cave = list(map(str.strip, sys.stdin))
    print(energized_tiles(cave, (-1, 0), E))
