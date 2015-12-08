import re
with open("day5.txt") as f:
    lines = f.readlines()

count = 0
for i in lines:
    v = 0
    for c in i:
        v += 1 if c in "aeiou" else 0
    r = len(re.findall(r"(.)\1", i))
    if v >= 3 and r >= 1 and not any(s in i for s in ["ab", "cd", "pq", "xy"]):
        count += 1
print(count)
