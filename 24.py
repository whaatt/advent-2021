# mypy: ignore-errors
# flake8: noqa

from math import trunc

data = open("24-input.txt").read().strip().split("\n")


def run_program(instructions, inputs, steps):
    inputs_index = 0
    memory = {key: 0 for key in "wxyz"}
    for line in instructions:
        line = line.split(" ")
        if line[0] == "inp":
            if inputs_index == steps:
                break
            print(memory)
            memory[line[1]] = int(inputs[inputs_index])
            inputs_index += 1
        elif line[0] == "add":
            if line[2] not in "wxyz":
                memory[line[1]] = memory[line[1]] + int(line[2])
            else:
                memory[line[1]] = memory[line[1]] + memory[line[2]]
        elif line[0] == "mul":
            if line[2] not in "wxyz":
                memory[line[1]] = memory[line[1]] * int(line[2])
            else:
                memory[line[1]] = memory[line[1]] * memory[line[2]]
        elif line[0] == "div":
            if line[2] not in "wxyz":
                memory[line[1]] = trunc(memory[line[1]] / int(line[2]))
            else:
                memory[line[1]] = trunc(memory[line[1]] / memory[line[2]])
        elif line[0] == "mod":
            if line[2] not in "wxyz":
                memory[line[1]] = memory[line[1]] % int(line[2])
            else:
                memory[line[1]] = memory[line[1]] % memory[line[2]]
        elif line[0] == "eql":
            if line[2] not in "wxyz":
                memory[line[1]] = 1 if memory[line[1]] == int(line[2]) else 0
            else:
                memory[line[1]] = 1 if memory[line[1]] == memory[line[2]] else 0
    return memory


print(run_program(data, "91411143612181", 14))

"""
+3
+7
+1
shear -4, +6
+14
+7
shear -4, +9
shear -12, +9
+6
shear -11, +4
+0
shear -1, +7
shear 0, +12
shear -11, +1

##
w_0 + 3
w_0 + 3, w_1 + 7
w_0 + 3, w_1 + 7, w_2 + 1

# w_2 - 3 == w_3
w_0 + 3, w_1 + 7

##
w_0 + 3, w_1 + 7, w_4 + 14
w_0 + 3, w_1 + 7, w_4 + 14, w_5 + 7

# w_5 + 3 == w_6
w_0 + 3, w_1 + 7, w_4 + 14

# w_4 + 2 == w_7
w_0 + 3, w_1 + 7

##
w_0 + 3, w_1 + 7, w_8 + 6

# w_8 - 5 = w_9
w_0 + 3, w_1 + 7

##
w_0 + 3, w_1 + 7, w_10

# w_10 - 1 = w_11
w_0 + 3, w_1 + 7

# w_1 + 7 = w_12
w_0 + 3

# w_0 - 8 = w_13
# Empty

0   9   
1   1
2   4
3   1
4   1
5   1
6   4
7   3
8   6
9   1
10  2
11  1
12  8
13  1

"""
