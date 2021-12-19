# mypy: ignore-errors
# flake8: noqa

data = open("13-input.txt").read()
data = data.split("\n")[:-1]

# fold along x=655
# fold along y=447
# fold along x=327
# fold along y=223
# fold along x=163
# fold along y=111
# fold along x=81
# fold along y=55
# fold along x=40
# fold along y=27
# fold along y=13
# fold along y=6

coords = set([tuple(int(number) for number in row.split(",")) for row in data])


def fold_x(coords, value):
    max_x = max(coord[0] for coord in coords)
    offset = 0
    if max_x - value > value:
        offset = (max_x - value) - value
    new_coords = set()
    for coord in coords:
        if coord[0] < value:
            new_coords.add((coord[0] + offset, coord[1]))
        else:
            new_position = value - (coord[0] - value)
            new_coords.add((new_position + offset, coord[1]))
    return new_coords


def fold_y(coords, value):
    max_y = max(coord[1] for coord in coords)
    offset = 0
    if max_y - value > value:
        offset = (max_y - value) - value
    new_coords = set()
    for coord in coords:
        if coord[1] < value:
            new_coords.add((coord[0], coord[1] + offset))
        else:
            new_position = value - (coord[1] - value)
            new_coords.add((coord[0], new_position + offset))
    return new_coords


folds = [
    (False, 655),
    (True, 447),
    (False, 327),
    (True, 223),
    (False, 163),
    (True, 111),
    (False, 81),
    (True, 55),
    (False, 40),
    (True, 27),
    (True, 13),
    (True, 6),
]

for (is_y, value) in folds:
    if is_y:
        coords = fold_y(coords, value)
    else:
        coords = fold_x(coords, value)

max_x = max(coord[0] for coord in coords)
max_y = max(coord[1] for coord in coords)

for x in range(max_x + 1):
    for y in range(max_y + 1):
        if (x, y) in coords:
            print("#", end="")
        else:
            print(".", end="")
    print()
