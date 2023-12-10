#!/usr/bin/env python3

import sys

N = ( 0, -1)
E = (+1,  0)
S = ( 0, +1)
W = (-1,  0)

directions_by_symbol = {
    '|': {N, S},
    '-': {E, W},
    'L': {N, E},
    'J': {N, W},
    '7': {S, W},
    'F': {S, E},
}

def parse_maze(lines):
    maze = {}
    for y, line in enumerate(lines):
        for x, symbol in enumerate(line.strip()):
            maze[(x, y)] = symbol
    return maze

def find_start_location(maze):
    for location, symbol in maze.items():
        if symbol == 'S':
            return location

def find_loop(maze):
    start = find_start_location(maze)
    for symbol in directions_by_symbol.keys():
        maze[start] = symbol
        loop = set()
        for location in follow_maze(start, maze):
            loop.add(location)
            if location == start:
                return loop

def find_connections(location, maze):
    x, y = location
    symbol = maze[location]
    for xd, yd in directions_by_symbol[symbol]:
        opposite_direction = (-xd, -yd)
        connected_location = (x+xd, y+yd)
        if connected_location in maze:
            connected_symbol = maze[connected_location]
            if opposite_direction in directions_by_symbol[connected_symbol]:
                yield connected_location

def follow_maze(start, maze):
    location = start
    connections = set(find_connections(location, maze))
    while connections:
        connection = next(iter(connections))
        connections = set(find_connections(connection, maze))
        if location not in connections:
            break
        connections.remove(location)
        location = connection
        yield location

if __name__ == '__main__':
    maze = parse_maze(sys.stdin)
    loop = find_loop(maze)
    print(len(loop) // 2)
