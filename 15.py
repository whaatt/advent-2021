# mypy: ignore-errors
# flake8: noqa


def inc_wrap(i, inc):
    i = i + inc
    if i >= 10:
        i %= 9
    return i


data = open("15-input.txt").read()
data = data.split("\n")[:-1]
data = [
    [int(i) for i in row]
    + [inc_wrap(int(i), 1) for i in row]
    + [inc_wrap(int(i), 2) for i in row]
    + [inc_wrap(int(i), 3) for i in row]
    + [inc_wrap(int(i), 4) for i in row]
    for row in data
]

data_length = len(data)
for inc in range(1, 5):
    for j in range(data_length):
        data.append([inc_wrap(int(i), inc) for i in data[j]])

import heapq
from collections import defaultdict

seen = set()
heap = []
dist = defaultdict(lambda: float("inf"))

heapq.heappush(heap, (0, (0, 0)))
dist[0, 0] = 0

while heap:
    risk, (i, j) = heapq.heappop(heap)
    if (i, j) in seen:
        continue
    if i == len(data) - 1 and j == len(data[i]) - 1:
        print(dist[i, j])
        break
    seen.add((i, j))
    for (x, y) in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= x < len(data) and 0 <= y < len(data[i]) and (x, y) not in seen:
            dist[x, y] = min(dist[x, y], risk + data[x][y])
            heapq.heappush(heap, (dist[x, y], (x, y)))
