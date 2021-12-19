# mypy: ignore-errors
# flake8: noqa

data = open("11-input.txt").read()
data = data.split("\n")[:-1]
matrix = [[int(char) for char in row] for row in data]

seen = set()


def get_neighbors(i, j):
    possible = [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j - 1),
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1),
    ]
    possible = [
        (x, y)
        for (x, y) in possible
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[x])
    ]
    possible = [point for point in possible if point not in seen]
    return possible


step = 1
while True:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += 1
    seen = set()
    while True:
        found_greater = False
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] > 9:
                    matrix[i][j] = 0
                    seen.add((i, j))
                    for (x, y) in get_neighbors(i, j):
                        matrix[x][y] += 1
                    found_greater = True
        if not found_greater:
            break
    found_same = True
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != matrix[0][0]:
                found_same = False
                break
        if not found_same:
            break
    if found_same:
        print(step)
        break
    step += 1
