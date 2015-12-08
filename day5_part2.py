import re
with open("day5.txt") as f:
    lines = f.readlines()

count = 0
for i in lines:
    p = len(re.findall(r"(..).*\1", i))
    r = len(re.findall(r"(.).\1", i))
    if p >= 1 and r >= 1:
        count += 1
print(count)
