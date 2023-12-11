#!/usr/bin/env python3

import sys

def find_galaxies(lines):
    for row, line in enumerate(lines):
        for column, cell in enumerate(line):
            if cell == '#':
                yield row, column

def expand_cosmos(galaxies, expansion=2):
    galaxy_rows = set(row for row, column in galaxies)
    galaxy_columns = set(column for row, column in galaxies)
    rows = set(range(min(galaxy_rows), max(galaxy_rows) + 1))
    columns = set(range(min(galaxy_columns), max(galaxy_columns) + 1))
    expanding_rows = rows - galaxy_rows
    expanding_columns = columns - galaxy_columns
    expanded_row = 0
    for row in rows:
        if row in expanding_rows:
            expanded_row += expansion
        else:
            expanded_column = 0
            for column in columns:
                if column in expanding_columns:
                    expanded_column += expansion
                else:
                    if (row, column) in galaxies:
                        yield expanded_row, expanded_column
                    expanded_column += 1
            expanded_row += 1

def distances_between_galaxies(galaxies):
    for i, (x1, y1) in enumerate(galaxies):
        for j, (x2, y2) in enumerate(galaxies):
            if i < j:
                yield abs(x1 - x2) + abs(y1 - y2)

if __name__ == '__main__':
    image = list(line.strip() for line in sys.stdin)
    galaxies = set(find_galaxies(image))
    expanded_galaxies = set(expand_cosmos(galaxies))
    print(sum(distances_between_galaxies(expanded_galaxies)))
