#!/usr/bin/env python3

from part1 import parse_almanac

import sys

def convert_range(start, end, mapping):
    for (source, length), destination in mapping.items():
        if (source <= start and start < source + length) or (source < end and end <= source + length):
            if start < source:
                for mapped_range in convert_range(start, source, mapping):
                    yield mapped_range
            mapped_start = destination + (max(start, source) - source)
            mapped_end = destination + (min(source + length, end) - source)
            yield mapped_start, mapped_end
            if source + length < end:
                for mapped_range in convert_range(source + length, end, mapping):
                    yield mapped_range
            return
    yield start, end

def range_conversions(categories, mappings):
    mapped_categories = {}
    for category, ranges in categories.items():
        for start, end in ranges:
            for mapped_category, mapping in mappings[category].items():
                mapped_categories.setdefault(mapped_category, []).extend(convert_range(start, end, mapping))
    return mapped_categories

def find_range_conversions(ranges, source, destination, mappings):
    categories = {source: ranges}
    while destination not in categories:
        categories = range_conversions(categories, mappings)
    return categories[destination]

def location_ranges_for_seeds(seed_ranges, mappings):
    return find_range_conversions(seed_ranges, 'seed', 'location', mappings)

if __name__ == '__main__':
    seeds, mappings = parse_almanac(sys.stdin)
    seed_ranges = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
    print(min(start for start, end in location_ranges_for_seeds(seed_ranges, mappings)))
