# mypy: ignore-errors
# flake8: noqa


def simulate(vx, vy, steps):
    x, y = 0, 0
    for _ in range(steps):
        x += vx
        y += vy
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1
    return x, y


xmin, xmax = 94, 151
ymin, ymax = -156, -103

vxmin, vxmax = 14, 151
vymin, vymax = -156, 1000

distinct = set()
for vx in range(vxmin, vxmax + 1):
    for vy in range(-156, 400):
        for steps in range(313):
            x, y = simulate(vx, vy, steps)
            if xmin <= x <= xmax and ymin <= y <= ymax:
                distinct.add((vx, vy))
            if x > xmax or y < ymin:
                break

print(len(distinct))

# vxmin, vxmax = 1, 300
# for vy in range(1, 30):
#     print("vy:", vy)
#     min_steps = float("inf")
#     max_steps = float("-inf")
#     for vx in range(vxmin, vxmax + 1):
#         last_x = None
#         steps = 1
#         while True:
#             x, y, max_y = simulate(vx, vy, steps)
#             if xmin <= x <= xmax and ymin <= y <= ymax:
#                 print("steps\t", steps, "\tresult\t", (x, y, max_y))
#             if x > xmax or x == last_x:
#                 break
#             last_x = x
#             steps += 1
#         if steps < min_steps:
#             min_steps = steps
#         if steps > max_steps:
#             max_steps = steps
#     print(min_steps, max_steps)
