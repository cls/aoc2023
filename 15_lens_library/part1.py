#!/usr/bin/env python3

import sys

def holiday_hash(string):
    value = 0
    for char in string:
        value += ord(char)
        value *= 17
        value %= 256
    return value

if __name__ == '__main__':
    init_sequence = next(sys.stdin).strip().split(',')
    print(sum(map(holiday_hash, init_sequence)))
