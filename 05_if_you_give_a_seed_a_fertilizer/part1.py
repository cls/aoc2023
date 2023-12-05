#!/usr/bin/env python3

import sys

def parse_almanac(lines):
    seeds = []
    mappings = {}
    mapping = None
    for line in lines:
        words = line.split()
        if len(words) > 0 and words[0] == 'seeds:':
            seeds.extend(map(int, words[1:]))
        elif len(words) == 2 and words[1] == 'map:':
            source, destination = words[0].split('-to-')
            mapping = mappings.setdefault(source, {}).setdefault(destination, {})
        elif words:
            destination, source, length = map(int, words)
            mapping[(source, length)] = destination
    return seeds, mappings

def convert(value, mapping):
    for (source, length), destination in mapping.items():
        if source <= value and value < source + length:
            mapped_value = destination + (value - source)
            return mapped_value
    return value

def conversions(categories, mappings):
    mapped_categories = {}
    for category, value in categories.items():
        for mapped_category, mapping in mappings[category].items():
            mapped_categories[mapped_category] = convert(value, mapping)
    return mapped_categories

def find_conversion(value, source, destination, mappings):
    categories = {source: value}
    while destination not in categories:
        categories = conversions(categories, mappings)
    return categories[destination]

def locations_for_seeds(seeds, mappings):
    for seed in seeds:
        location = find_conversion(seed, 'seed', 'location', mappings)
        yield location

if __name__ == '__main__':
    seeds, mappings = parse_almanac(sys.stdin)
    print(min(locations_for_seeds(seeds, mappings)))
