with open("day6.txt") as f:
    lines = f.readlines()

grid = [[0 for _ in range(1000)] for _ in range(1000)]

for i in lines:
    i = i.split(" ")
    com = i[1] if i[1] in ["on", "off"] else "toggle"
    start = list(map(int, (i[1] if com == "toggle" else i[2]).split(",")))
    stop = list(map(int, (i[3] if com == "toggle" else i[4]).split(",")))

    for j in range(start[0], stop[0]+1):
        for k in range(start[1], stop[1]+1):
            if com == "on":
                grid[j][k] += 1
            elif com == "off" and grid[j][k] > 0:
                grid[j][k] -= 1
            elif com == "toggle":
                grid[j][k] += 2

print(sum(map(sum, grid)))
