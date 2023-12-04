#!/usr/bin/env python3

import re
import sys

scratchcard_pattern = re.compile('Card +(?P<card_id>\d+): (?P<numbers>.*) \| (?P<winners>.*)')

def parse_scratchcards(lines):
    cards = {}
    for line in lines:
        match = scratchcard_pattern.match(line)
        card_id = int(match.group('card_id'))
        numbers_str, winners_str = match.group('numbers', 'winners')
        numbers = set(map(int, numbers_str.split()))
        winners = set(map(int, winners_str.split()))
        cards[card_id] = (numbers, winners)
    return cards

def scratchcard_wins(card):
    numbers, winners = card
    wins = numbers & winners
    return wins

def scratchcard_points(card):
    wins = scratchcard_wins(card)
    points = 2 ** (len(wins) - 1) if wins else 0
    return points

if __name__ == '__main__':
    cards = parse_scratchcards(sys.stdin)
    print(sum(map(scratchcard_points, cards.values())))
