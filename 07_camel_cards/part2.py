#!/usr/bin/env python3

from part1 import parse_camel_cards, bids_by_rank

import sys

cards_with_jokers = 'J23456789TQKA'

def ranking_with_jokers(hand):
    counts = {}
    jokers = 0
    for card in hand:
        if card == 'J':
            jokers += 1
        else:
            counts[card] = counts.get(card, 0) + 1
    if not counts:
        counts['J'] = 0
    return -len(counts), max(counts.values()) + jokers, list(map(cards_with_jokers.index, hand))

if __name__ == '__main__':
    bids_by_hand = parse_camel_cards(sys.stdin)
    print(sum(rank * bid for rank, bid in bids_by_rank(bids_by_hand, ranking=ranking_with_jokers)))
