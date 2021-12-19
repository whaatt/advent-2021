# mypy: ignore-errors
# flake8: noqa

data = open("9-input.txt").read()
data = data.split("\n")[:-1]
data = [[int(item) for item in row] for row in data]


def get_basin_neighbors(i, j):
    neighbors = []
    if i != 0 and data[i - 1][j] != 9:
        neighbors.append((i - 1, j))
    if j != 0 and data[i][j - 1] != 9:
        neighbors.append((i, j - 1))
    if i != len(data) - 1 and data[i + 1][j] != 9:
        neighbors.append((i + 1, j))
    if j != len(data[0]) - 1 and data[i][j + 1] != 9:
        neighbors.append((i, j + 1))
    return neighbors


basins = {}
next_basin_number = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if (i, j) in basins or data[i][j] == 9:
            continue
        basins[i, j] = next_basin_number
        basin_stack = get_basin_neighbors(i, j)
        while basin_stack:
            x, y = basin_stack.pop()
            if (x, y) in basins:
                continue
            basins[x, y] = next_basin_number
            basin_stack.extend(get_basin_neighbors(x, y))
        next_basin_number += 1

from collections import defaultdict

basin_sizes = defaultdict(int)
for basin in basins.values():
    basin_sizes[basin] += 1

largest = sorted(basin_sizes.keys(), key=lambda size: basin_sizes[size], reverse=True)[
    :3
]
result = 1
for item in largest:
    result *= basin_sizes[item]
print(result)
