import operator
with open("day3.txt") as f:
    line = f.readline()

(x, y) = (0, 0)
grid = dict()
grid[(x, y)] = 1

opts = {
    "^": (0, 1),
    ">": (1, 0),
    "v": (0, -1),
    "<": (-1, 0)
}

for c in line:
    (x, y) = map(operator.add, (x, y), opts[c])

    try:
        grid[(x, y)] += 1
    except KeyError:
        grid[(x, y)] = 1

print(len({k: v for (k, v) in grid.items() if v > 0}))
