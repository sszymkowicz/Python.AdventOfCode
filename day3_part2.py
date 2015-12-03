import operator
with open("day3.txt") as f:
    line = f.readline()

(x_s, y_s) = (0, 0)
(x_rs, y_rs) = (0, 0)
grid = dict()
grid[(x_s, y_s)] = 1

opts = {
    "^": (0, 1),
    ">": (1, 0),
    "v": (0, -1),
    "<": (-1, 0)
}

for i, c in enumerate(line):
    if not i % 2:
        (x, y) = map(operator.add, (x_s, y_s), opts[c])
        (x_s, y_s) = (x, y)
    else:
        (x, y) = map(operator.add, (x_rs, y_rs), opts[c])
        (x_rs, y_rs) = (x, y)

    try:
        grid[(x, y)] += 1
    except KeyError:
        grid[(x, y)] = 1

print(len({k: v for (k, v) in grid.items() if v > 0}))
