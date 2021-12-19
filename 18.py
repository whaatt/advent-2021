# mypy: ignore-errors
# flake8: noqa

from copy import deepcopy
from math import ceil, floor

data = open("18-input.txt").read().split("\n")[:-1]
data = [eval(row) for row in data]


def get_at(value, position):
    position = position[:]
    for i in position:
        if type(value) == int:
            return None
        value = value[i]
    return value


def prev_pos(value, position):
    position = position[:]
    while True:
        if len(position) == 0:
            return None
        if position[-1] == 1:
            position[-1] = 0
            break
        if position[-1] == 0:
            position.pop()
    while True:
        position.append(1)
        if get_at(value, position) is not None:
            continue
        position.pop()
        position.append(0)
        if get_at(value, position) is not None:
            continue
        position.pop()
        return position


def next_pos(value, position):
    position = position[:]
    while True:
        if len(position) == 0:
            return None
        if position[-1] == 0:
            position[-1] = 1
            break
        if position[-1] == 1:
            position.pop()
    while True:
        position.append(0)
        if get_at(value, position) is not None:
            continue
        position.pop()
        position.append(1)
        if get_at(value, position) is not None:
            continue
        position.pop()
        return position


def first_pos(value):
    position = []
    while type(get_at(value, position)) != int:
        position.append(0)
    return position


def get_explode(value):
    pos = first_pos(value)
    while pos is not None:
        if len(pos) >= 5:
            return pos[:-1]
        pos = next_pos(value, pos)
    return None


def get_split(value):
    pos = first_pos(value)
    while pos is not None:
        if get_at(value, pos) >= 10:
            return pos
        pos = next_pos(value, pos)
    return None


def add(value_1, value_2):
    value = [deepcopy(value_1), deepcopy(value_2)]
    while True:
        explode = get_explode(value)
        if explode is not None:
            prev_explode = prev_pos(value, explode + [0])
            if prev_explode is not None:
                get_at(value, prev_explode[:-1])[prev_explode[-1]] += get_at(
                    value, explode + [0]
                )
            next_explode = next_pos(value, explode + [1])
            if next_explode is not None:
                get_at(value, next_explode[:-1])[next_explode[-1]] += get_at(
                    value, explode + [1]
                )
            get_at(value, explode[:-1])[explode[-1]] = 0
            continue
        split = get_split(value)
        if split is not None:
            get_at(value, split[:-1])[split[-1]] = [
                floor(get_at(value, split) / 2),
                ceil(get_at(value, split) / 2),
            ]
            continue
        return value


def magnitude(value):
    if type(value) == int:
        return value
    return 3 * magnitude(value[0]) + 2 * magnitude(value[1])


largest = float("-inf")
for row_1 in data:
    for row_2 in data:
        if row_1 != row_2:
            largest = max(largest, magnitude(add(row_1, row_2)))
print(largest)
