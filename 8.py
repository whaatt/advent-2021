# mypy: ignore-errors
# flake8: noqa

# length 2 -> 1
# length 4 -> 4
# length 3 -> 7
# length 7 -> 8
# length 5 -> 2, 3, 5
# length 6 -> 0, 6, 9

data = open("8-input.txt").read()
data = data.split("\n")[:-1]
data = [
    [
        ["".join(sorted(segment)) for segment in part.split(" ")]
        for part in line.split(" | ")
    ]
    for line in data
]


def overlap(x, y):
    return len(set(x) & set(y))


total = 0
for [input, output] in data:
    one_pattern = [number for number in input if len(number) == 2][0]
    four_pattern = [number for number in input if len(number) == 4][0]

    digits = ""
    for number in output:
        if len(number) == 2:
            digits += "1"
        elif len(number) == 4:
            digits += "4"
        elif len(number) == 3:
            digits += "7"
        elif len(number) == 7:
            digits += "8"
        elif len(number) == 6:
            if overlap(number, one_pattern) == 1:
                digits += "6"
            elif overlap(number, four_pattern) == 4:
                digits += "9"
            else:
                digits += "0"
        else:
            if overlap(number, one_pattern) == 2:
                digits += "3"
            elif overlap(number, four_pattern) == 3:
                digits += "5"
            else:
                digits += "2"
    total += int(digits)
print(total)
