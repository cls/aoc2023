#!/usr/bin/env python3

import operator
import re
import sys

from collections import namedtuple

Part = namedtuple('Part', ('x', 'm', 'a', 's'))

comparators = {
    '<': operator.lt,
    '>': operator.gt,
}

workflow_pattern = re.compile(r'(?P<name>[a-z]+)\{(?P<workflow>[^{}]+)\}')
step_pattern = re.compile(r'(?:(?P<rating>[xmas])(?P<comparator>[<>])(?P<value>\d+):)?(?P<destination>[AR]|[a-z]+)')

def make_mid_workflow(existing_workflow, rating, comparator, value, destination, workflows):
    return lambda part: workflows[destination](part) if comparator(getattr(part, rating), value) else existing_workflow(part)

def make_end_workflow(destination, workflows):
    return lambda part: workflows[destination](part)

def parse_workflows(lines):
    workflows = {
        'A': lambda part: True,
        'R': lambda part: False,
    }
    for line in map(str.strip, lines):
        if not line:
            break
        workflow_match = workflow_pattern.fullmatch(line)
        name, workflow_str = workflow_match.group('name', 'workflow')
        workflow = lambda part: None
        for step_str in reversed(workflow_str.split(',')):
            step_match = step_pattern.match(step_str)
            rating, comparator_str, value_str, destination = step_match.group('rating', 'comparator', 'value', 'destination')
            if rating:
                comparator = comparators[comparator_str]
                value = int(value_str)
                workflow = make_mid_workflow(workflow, rating, comparator, value, destination, workflows)
            else:
                workflow = make_end_workflow(destination, workflows)
        workflows[name] = workflow
    return workflows

part_pattern = re.compile(r'\{x=(?P<x>\d+),m=(?P<m>\d+),a=(?P<a>\d+),s=(?P<s>\d+)\}')

def parse_parts(lines):
    for line in map(str.strip, lines):
        part_match = part_pattern.fullmatch(line)
        x, m, a, s = map(int, part_match.group('x', 'm', 'a', 's'))
        yield Part(x, m, a, s)

def total_rating(part):
    return part.x + part.m + part.a + part.s

if __name__ == '__main__':
    workflows = parse_workflows(sys.stdin)
    parts = parse_parts(sys.stdin)
    accepted = workflows['in']
    print(sum(map(total_rating, filter(accepted, parts))))
