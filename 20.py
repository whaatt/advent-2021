# mypy: ignore-errors
# flake8: noqa

data = open("20-input.txt").read().strip().split("\n")
data = [[1 if char == "#" else 0 for char in row] for row in data]

enhance_string = "#.#.#...###..#.##...######..###..#...#.#.#.##.##.#.#.#..##..#..###...#..#.#.#.#.#....##.##..#....##...#..#.###.###.##...####...##....#..#..#.#.###...#.#..##..#.#.......#...###..####..##..##.##.###..#.#...##...#.###.#..##..####.#.......###...####.#.#....#.#.#.#.##.##.####..#..#..##..#......##.....#..#.#..#..#.##.########.........#.###.#####...##.#...####.#..#.#..#....#.##...##.##.#.##.##......####.###.#..##.#..###.##..###.#.###...######.#######...#..##...#.......###..#.####.#.####.#.#......#.#.#.#...#..###.."
enhance_values = [1 if char == "#" else 0 for char in enhance_string]


def enhance(matrix, parity):
    output = [[0 for _ in range(len(matrix[0]) + 2)] for _ in range(len(matrix) + 2)]
    for i in range(-1, len(matrix) + 1):
        for j in range(-1, len(matrix[0]) + 1):
            binary = ""
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                        binary += str(matrix[x][y])
                    else:
                        binary += str(parity)
            value = enhance_values[int(binary, 2)]
            output[i + 1][j + 1] = value
    return output


def print_data(matrix):
    for row in matrix:
        for char in row:
            print(char, end="")
        print()


current = data
for i in range(50):
    current = enhance(current, i % 2)
print(sum(sum(row) for row in current))
