# mypy: ignore-errors
# flake8: noqa

from collections import Counter, defaultdict
from functools import cache, reduce
from itertools import product
from operator import add

triple_rolls = Counter(reduce(add, value, 0) for value in product(*[[1, 2, 3]] * 3))

ways_to_reach = defaultdict(set)
# (rolls, p1_score, p2_score, p1, p2, is_p1_turn) = source_set
ways_to_reach[0, 0, 0, 8, 4, True] = set()

current_rolls = 0
while True:
    non_winning_states = {
        state
        for state in ways_to_reach
        if state[0] == current_rolls and state[1] < 21 and state[2] < 21
    }
    if len(non_winning_states) == 0:
        break
    for state in non_winning_states:
        (_, p1_score, p2_score, p1, p2, is_p1_turn) = state
        for roll, count in triple_rolls.items():
            if is_p1_turn:
                p1_new = (p1 + roll) % 10
                if p1_new == 0:
                    p1_new = 10
                p1_score_new = p1_score + p1_new
                ways_to_reach[
                    current_rolls + 1, p1_score_new, p2_score, p1_new, p2, False
                ].add((state, count))
            else:
                p2_new = (p2 + roll) % 10
                if p2_new == 0:
                    p2_new = 10
                p2_score_new = p2_score + p2_new
                ways_to_reach[
                    current_rolls + 1, p1_score, p2_score_new, p1, p2_new, True
                ].add((state, count))
    current_rolls += 1


@cache
def get_ways_to_reach_count(destination):
    if len(ways_to_reach[destination]) == 0:
        return 1
    total_ways = 0
    for (source, count) in ways_to_reach[destination]:
        total_ways += count * get_ways_to_reach_count(source)
    return total_ways


total_ways_1 = 0
total_ways_2 = 0
for state in ways_to_reach:
    if state[1] >= 21:
        total_ways_1 += get_ways_to_reach_count(state)
    elif state[2] >= 21:
        total_ways_2 += get_ways_to_reach_count(state)
print(max(total_ways_1, total_ways_2))
