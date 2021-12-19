# mypy: ignore-errors
# flake8: noqa

from collections import Counter
from functools import cache


def points_to_list(points_string):
    return tuple(eval("(" + row + ")") for row in points_string.strip().split("\n"))


@cache
def get_transformed_lists(point_list):
    rotate_lists = [point_list]
    for _ in range(3):
        rotate_lists.append(
            tuple((point[0], point[2], -point[1]) for point in rotate_lists[-1])
        )
    final_lists = []
    for point_list in rotate_lists:
        final_lists.append(point_list)
        start_index = len(final_lists) - 1
        for _ in range(3):
            final_lists.append(
                tuple((point[1], -point[0], point[2]) for point in final_lists[-1])
            )
        final_lists.append(
            tuple((point[2], point[1], -point[0]) for point in final_lists[start_index])
        )
        final_lists.append(
            tuple((-point[2], point[1], point[0]) for point in final_lists[start_index])
        )
    return tuple(final_lists)


@cache
def add(x, y):
    return (x[0] + y[0], x[1] + y[1], x[2] + y[2])


@cache
def sub(x, y):
    return (x[0] - y[0], x[1] - y[1], x[2] - y[2])


data = open("19-input.txt").read().strip().split("\n\n")
lists = [points_to_list(points_string) for points_string in data]


@cache
def get_max_displacement(list_0, list_1):
    displacements = Counter(
        sub(point_0, point_1)
        for scanner_1_transform in get_transformed_lists(list_1)
        for point_0 in list_0
        for point_1 in scanner_1_transform
    )
    max_displacement, count = displacements.most_common(1)[0]
    top_lists = Counter(
        scanner_1_transform
        for scanner_1_transform in get_transformed_lists(list_1)
        for point_0 in list_0
        for point_1 in scanner_1_transform
        if sub(point_0, point_1) == max_displacement
    )
    top_list, _ = top_lists.most_common(1)[0]
    return top_list, max_displacement, count


displacement = {0: (0, 0, 0)}
while len(displacement) < len(lists):
    for i in range(len(lists)):
        if i not in displacement:
            continue
        for j in range(len(lists)):
            if i == j or j in displacement:
                continue
            top_list, max_displacement, count = get_max_displacement(lists[i], lists[j])
            if count >= 12:
                lists[j] = top_list
                displacement[j] = add(displacement[i], max_displacement)


# beacons = set()
# for i in range(len(lists)):
#     for point in lists[i]:
#         beacons.add(add(point, displacement[i]))
# print(len(beacons))

print(
    max(
        [
            sum(abs(i) for i in sub(value_1, value_0))
            for value_0 in displacement.values()
            for value_1 in displacement.values()
        ]
    )
)
