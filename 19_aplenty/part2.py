#!/usr/bin/env python3

from part1 import Part, comparators, workflow_pattern, step_pattern

import operator
import sys

def make_mid_range_workflow(existing_workflow, rating, comparator, value, destination, workflows):
    def workflow(parts):
        count = 0
        start, end = getattr(parts, rating)
        if comparator is operator.lt:
            if start < value:
                count += workflows[destination](parts._replace(**{rating: (start, min(value - 1, end))}))
            if not (end < value):
                count += existing_workflow(parts._replace(**{rating: (max(start, value), end)}))
        elif comparator is operator.gt:
            if end > value:
                count += workflows[destination](parts._replace(**{rating: (max(start, value + 1), end)}))
            if not (start > value):
                count += existing_workflow(parts._replace(**{rating: (start, min(value, end))}))
        return count
    return workflow

def make_end_range_workflow(destination, workflows):
    return lambda parts: workflows[destination](parts)

def total_range(parts):
    return (parts.x[1] - parts.x[0] + 1) * (parts.m[1] - parts.m[0] + 1) * (parts.a[1] - parts.a[0] + 1) * (parts.s[1] - parts.s[0] + 1)

def parse_range_workflows(lines):
    workflows = {
        'A': lambda parts: total_range(parts),
        'R': lambda parts: 0,
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
                workflow = make_mid_range_workflow(workflow, rating, comparator, value, destination, workflows)
            else:
                workflow = make_end_range_workflow(destination, workflows)
        workflows[name] = workflow
    return workflows

if __name__ == '__main__':
    range_workflows = parse_range_workflows(sys.stdin)
    accepted = range_workflows['in']
    full_range = (1, 4000)
    all_parts = Part(full_range, full_range, full_range, full_range)
    print(accepted(all_parts))
