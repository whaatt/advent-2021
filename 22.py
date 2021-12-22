# mypy: ignore-errors
# flake8: noqa

from functools import cache, reduce
from operator import mul

data = open("22-input.txt").read().strip().split("\n")


def parse_line(line):
    [state, rest] = line.split(" ")
    intervals = rest.split(",")
    intervals = [interval.split("=")[1] for interval in intervals]
    intervals = tuple(
        (int(interval.split("..")[0]), int(interval.split("..")[1]) + 1)
        for interval in intervals
    )
    return ((True if state == "on" else False), intervals)


@cache
def interval_overlap_1d(a, b):
    c = min(a, b)
    d = max(a, b)
    if d[0] >= c[1]:
        return None
    if d[1] > c[1]:
        return (d[0], c[1])
    return (d[0], d[1])


@cache
def intervals_overlap(a, b):
    overlap = tuple(interval_overlap_1d(a[i], b[i]) for i in range(len(a)))
    if None in overlap:
        return None
    return overlap


@cache
def interval_size_1d(a):
    return a[1] - a[0]


@cache
def intervals_size(a):
    return reduce(mul, (interval_size_1d(a[i]) for i in range(len(a))), 1)


total_on = 0
intervals_actions = []
data = [parse_line(line) for line in data]
for (turn_on, intervals) in data:
    new_actions = []
    # Zero-out all actions overlapping with the region.
    for (turn_on_other, intervals_other) in intervals_actions:
        overlap = intervals_overlap(intervals, intervals_other)
        if overlap is None:
            continue
        if turn_on_other:
            total_on -= intervals_size(overlap)
            new_actions.append((False, overlap))
        else:
            total_on += intervals_size(overlap)
            new_actions.append((True, overlap))
    # Increment the region as an action.
    if turn_on:
        total_on += intervals_size(intervals)
        new_actions.append((True, intervals))
    # Save the actions.
    intervals_actions.extend(new_actions)

print(total_on)
