# mypy: ignore-errors
# flake8: noqa

from copy import deepcopy

data = open("25-input.txt").read().strip().split("\n")
data = [[character for character in row] for row in data]
rows = len(data)
columns = len(data[0])

steps = 0
got_movement = True
while got_movement:
    steps += 1
    # print(steps)
    # print("\n".join("".join(row) for row in data))
    # print()
    got_movement = False
    new_data = deepcopy(data)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == ">" and data[i][(j + 1) % columns] == ".":
                got_movement = True
                new_data[i][j] = "."
                new_data[i][(j + 1) % columns] = ">"
    data = new_data
    new_data = deepcopy(data)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "v" and data[(i + 1) % rows][j] == ".":
                got_movement = True
                new_data[i][j] = "."
                new_data[(i + 1) % rows][j] = "v"
    data = new_data

print(steps)
