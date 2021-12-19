# mypy: ignore-errors
# flake8: noqa

fishes = open("6-input.txt").read()
fishes = fishes.split(",")
fishes = [int(i) for i in fishes]

# days_elapsed = 0
# while days_elapsed < 80:
#     new_fishes = []
#     for i in range(len(fishes)):
#         if fishes[i] > 0:
#             fishes[i] -= 1
#         else:
#             fishes[i] = 6
#             new_fishes.append(8)
#     fishes += new_fishes
#     days_elapsed += 1
#     print(days_elapsed, len(fishes))

day_counts = [0] * 9
for fish in fishes:
    day_counts[fish] += 1

days_elapsed = 0
while days_elapsed < 256:
    zero_count = day_counts.pop(0)
    day_counts[6] += zero_count
    day_counts.append(zero_count)
    days_elapsed += 1
    print(days_elapsed, sum(day_counts))
