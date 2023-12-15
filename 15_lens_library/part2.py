#!/usr/bin/env python3

from part1 import holiday_hash

import re
import sys

step_pattern = re.compile(r'(?P<label>[^-=]*)(?:-|=(?P<lens>\d+))')

def build_lens_library(sequence):
    boxes = [{} for box_number in range(256)]
    for step in sequence:
        match = step_pattern.fullmatch(step)
        label, lens_str = match.group('label', 'lens')
        box = boxes[holiday_hash(label)]
        if lens_str:
            box[label] = int(lens_str)
        elif label in box:
            del box[label]
    return boxes

def focusing_powers(boxes):
    for box_number, box in enumerate(boxes):
        for slot_number, lens in enumerate(box.values(), 1):
            yield (box_number + 1) * slot_number * lens

if __name__ == '__main__':
    init_sequence = next(sys.stdin).strip().split(',')
    lens_library = build_lens_library(init_sequence)
    print(sum(focusing_powers(lens_library)))
