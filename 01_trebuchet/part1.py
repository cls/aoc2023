#!/usr/bin/env python3

import sys

def calibration_value(line):
    digits = ''.join(filter(str.isdigit, line))
    value = int(digits[0] + digits[-1])
    return value

if __name__ == '__main__':
    print(sum(map(calibration_value, sys.stdin)))
