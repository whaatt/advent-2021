# mypy: ignore-errors
# flake8: noqa

from collections import defaultdict

data = open("14-input.txt").read()
data = data.split("\n")[:-1]
data = [tuple(row.split(" -> ")) for row in data]
substitutions = {key: value for (key, value) in data}

current = "CFFPOHBCVVNPHCNBKVNV"

pair_counts = defaultdict(int)
for i in range(len(current) - 1):
    pair_counts[current[i : i + 2]] += 1

char_counts = defaultdict(int)
for i in range(len(current)):
    char_counts[current[i]] += 1

for i in range(40):
    new_pair_counts = defaultdict(int)
    for key in pair_counts:
        if key in substitutions:
            new_char = substitutions[key]
            new_pair_counts[key[0] + new_char] += pair_counts[key]
            new_pair_counts[new_char + key[1]] += pair_counts[key]
            char_counts[new_char] += pair_counts[key]
    pair_counts = new_pair_counts

sorted_keys = sorted(char_counts.keys(), key=lambda x: char_counts[x])
print(char_counts[sorted_keys[-1]] - char_counts[sorted_keys[0]])
