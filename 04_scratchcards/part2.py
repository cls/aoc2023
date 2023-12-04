#!/usr/bin/env python3

from part1 import parse_scratchcards, scratchcard_wins

import sys

def recursive_scratchcards(cards):
    counts = dict.fromkeys(cards, 1)
    for card_id, card in cards.items():
        count = counts[card_id]
        wins = scratchcard_wins(card)
        for new_card_id, win in enumerate(wins, card_id + 1):
            if new_card_id in counts:
                counts[new_card_id] += count
    return counts

if __name__ == '__main__':
    cards = parse_scratchcards(sys.stdin)
    print(sum(recursive_scratchcards(cards).values()))
