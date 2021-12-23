# mypy: ignore-errors
# flake8: noqa

import heapq
from collections import defaultdict

data = """
#############
#..X.X.X.X..#
###D#C#A#B###
###D#C#B#A###
###D#B#A#C###
###C#D#A#B###
#############
""".strip().split(
    "\n"
)

matrix = {}
for i in range(len(data)):
    for j in range(len(data[i])):
        matrix[i, j] = data[i][j]

destination_column_map = {"A": 3, "B": 5, "C": 7, "D": 9}
move_value_map = {"A": 1, "B": 10, "C": 100, "D": 1000}


def get_moves(state, position):
    letter = state[position]
    if letter not in "ABCD":
        return []
    multiplier = move_value_map[letter]
    (row, column) = position
    # In a nook.
    if row > 1:
        # Nook tops are blocking nook bottoms.
        if "".join(state[i, column] for i in range(2, row)) != "." * (row - 2):
            return []
        moves_to_leave_count = row - 1
        moves = []
        # Try moving left from nook top.
        j = column
        while True:
            j -= 1
            if state[1, j] in "#ABCD":
                break
            if state[1, j] == ".":
                total_moves_count = moves_to_leave_count + abs(column - j)
                moves.append(((1, j), total_moves_count * multiplier))
        # Try moving right from nook top.
        j = column
        while True:
            j += 1
            if state[1, j] in "#ABCD":
                break
            if state[1, j] == ".":
                total_moves_count = moves_to_leave_count + abs(column - j)
                moves.append(((1, j), total_moves_count * multiplier))
        return moves
    # In the hallway.
    else:
        destination_column = destination_column_map[letter]
        j = column
        total_moves_count = 0
        # Move back to destination column.
        while j != destination_column:
            if j < destination_column:
                j += 1
            else:
                j -= 1
            total_moves_count += 1
            if state[1, j] in "#ABCD":
                return []
        # Hardcoded logic that could be easily extended to arbitrary columns for placement.
        slot_values = "".join(state[i, destination_column] for i in range(2, 6))
        if slot_values == "." + (letter * 3):
            total_moves_count += 1
            return [((2, destination_column), total_moves_count * multiplier)]
        elif slot_values == ".." + (letter * 2):
            total_moves_count += 2
            return [((3, destination_column), total_moves_count * multiplier)]
        elif slot_values == "..." + letter:
            total_moves_count += 3
            return [((4, destination_column), total_moves_count * multiplier)]
        elif slot_values == "....":
            total_moves_count += 4
            return [((5, destination_column), total_moves_count * multiplier)]
        else:
            return []


def to_string(state):
    return (
        "".join(state[1, j] for j in range(1, 12))
        + " "
        + (
            state[2, 3]
            + state[3, 3]
            + state[4, 3]
            + state[5, 3]
            + state[2, 5]
            + state[3, 5]
            + state[4, 5]
            + state[5, 5]
            + state[2, 7]
            + state[3, 7]
            + state[4, 7]
            + state[5, 7]
            + state[2, 9]
            + state[3, 9]
            + state[4, 9]
            + state[5, 9]
        )
    )


def solved(state):
    return to_string(state) == "..X.X.X.X.. AAAABBBBCCCCDDDD"


seen = set()
matrix_string = to_string(matrix)
states_by_string = {matrix_string: matrix}
states = [(0, matrix_string)]

min_total_moves_count = float("inf")
while states:
    total_moves_count, state_string = heapq.heappop(states)
    if state_string in seen:
        continue
    seen.add(state_string)
    state = states_by_string[state_string]
    if solved(state):
        min_total_moves_count = min(min_total_moves_count, total_moves_count)
        continue

    # Try moving all known positions.
    state_string = to_string(state)
    for (i, j) in state:
        for ((i_prime, j_prime), next_moves_count) in get_moves(state, (i, j)):
            new_state = state.copy()
            new_state[i_prime, j_prime], new_state[i, j] = new_state[i, j], "."
            new_moves_count = total_moves_count + next_moves_count
            new_state_string = to_string(new_state)

            # Add unseen states to stack.
            if new_state_string not in seen:
                states_by_string[new_state_string] = new_state
                heapq.heappush(states, (new_moves_count, new_state_string))

print(min_total_moves_count)
