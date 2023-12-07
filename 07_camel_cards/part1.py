#!/usr/bin/env python3

import sys

def parse_camel_cards(lines):
    bids_by_hand = {}
    for line in lines:
        hand, bid_str = line.split()
        bid = int(bid_str)
        bids_by_hand[hand] = bid
    return bids_by_hand

cards = '23456789TJQKA'

def ranking(hand):
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1
    return -len(counts), max(counts.values()), list(map(cards.index, hand))

def bids_by_rank(bids_by_hand, ranking=ranking):
    for rank, hand in enumerate(sorted(bids_by_hand.keys(), key=ranking), 1):
        yield rank, bids_by_hand[hand]

if __name__ == '__main__':
    bids_by_hand = parse_camel_cards(sys.stdin)
    print(sum(rank * bid for rank, bid in bids_by_rank(bids_by_hand)))
