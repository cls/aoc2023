#!/usr/bin/env python3

import re
import sys

wordy_digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

digit_pattern_str = r'(?P<digit>[0-9]|' + r'|'.join(wordy_digits.keys()) + r')'
first_digit_pattern = re.compile(r'.*?' + digit_pattern_str)
last_digit_pattern = re.compile(r'.*' + digit_pattern_str)

def get_wordy_digit(pattern, line):
    match = pattern.match(line)
    digit = match.group('digit')
    if not digit.isdigit():
        digit = wordy_digits[digit]
    return digit

def wordy_calibration_value(line):
    first_digit = get_wordy_digit(first_digit_pattern, line)
    last_digit = get_wordy_digit(last_digit_pattern, line)
    value = int(first_digit + last_digit)
    return value

if __name__ == '__main__':
    print(sum(map(wordy_calibration_value, sys.stdin)))
