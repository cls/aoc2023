#!/usr/bin/env python3

from part1 import S, E, parse_maze, find_loop

import sys

accessible_by_symbol = {
    '|': {S},
    '-': {E},
    'L': {S},
    'J': set(),
    '7': {E},
    'F': {S, E},
    '.': {S, E},
}

class UnionFind:
    def __init__(self):
        self._parents = {}
        self._ranks = {}

    def add(self, key):
        if key not in self._parents:
            self._parents[key] = key
            self._ranks[key] = 0

    def union(self, key1, key2):
        root1 = self.find(key1)
        root2 = self.find(key2)
        if root1 == root2:
            return
        rank1 = self._ranks[key1]
        rank2 = self._ranks[key2]
        if rank1 < rank2:
            root1, root2 = root2, root1
            rank1, rank2 = rank2, rank1
        self._parents[root2] = root1
        if rank1 == rank2:
            self._ranks[root1] = rank1 + 1

    def find(self, key):
        while key != self._parents[key]:
            key = self._parents[key]
        return key

    def sets(self):
        sets_by_root = {}
        for key in self._parents.keys():
            root = self.find(key)
            sets_by_root.setdefault(root, {root}).add(key)
        return sets_by_root.values()

def find_areas(maze):
    union_find = UnionFind()
    for location, symbol in maze.items():
        x, y = location
        union_find.add(location)
        for xd, yd in accessible_by_symbol[symbol]:
            connected_location = (x+xd, y+yd)
            union_find.add(connected_location)
            union_find.union(location, connected_location)
    return union_find

def find_contained_area(maze):
    union_find = find_areas(maze)
    max_x, max_y = max(maze.keys())
    for area in union_find.sets():
        if not any(x == 0 or x > max_x or y == 0 or y > max_y for x, y in area):
            return area

def extract_loop(maze):
    loop = find_loop(maze)
    for location in maze.keys():
        if location not in loop:
            maze[location] = '.'
    return loop

if __name__ == '__main__':
    maze = parse_maze(sys.stdin)
    loop = extract_loop(maze)
    print(len(find_contained_area(maze) - loop))
