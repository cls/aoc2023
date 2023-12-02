#!/usr/bin/env python3

import re
import sys

game_pattern = re.compile(r'Game (?P<game_id>\d+): (?P<game>.*)')

def parse_cube_games(lines):
    games = {}
    for line in lines:
        match = game_pattern.match(line)
        game_id_str, game_str = match.group('game_id', 'game')
        game_id = int(game_id_str)
        game = []
        for cubes_str in game_str.split('; '):
            cubes = {}
            for cube_str in cubes_str.split(', '):
                count_str, color = cube_str.split(' ')
                count = int(count_str)
                cubes[color] = count
            game.append(cubes)
        games[game_id] = game
    return games

def cube_game_is_possible(game, bag):
    for cubes in game:
        for color, count in cubes.items():
            if bag.get(color, 0) < count:
                return False
    return True

cube_bag = {'red': 12, 'green': 13, 'blue': 14}

if __name__ == '__main__':
    games = parse_cube_games(sys.stdin)
    print(sum(game_id for game_id, game in games.items() if cube_game_is_possible(game, cube_bag)))
