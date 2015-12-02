import re

boxes = list()
with open("day2.txt") as f:
    lines = f.readlines()

paper_out = 0
ribbon_out = 0
for i in lines:
    boxes.append(list(map(int, re.findall(r'[1-9][0-9]*', i))))
    paper_out += 2*boxes[-1][0]*boxes[-1][1] + 2*boxes[-1][0]*boxes[-1][2] + 2*boxes[-1][1]*boxes[-1][2]
    ribbon_out += boxes[-1][0]*boxes[-1][1]*boxes[-1][2]
    ribbon_out += 2*min(boxes[-1])
    a = min(boxes[-1])
    boxes[-1].remove(min(boxes[-1]))
    ribbon_out += 2*min(boxes[-1])
    b = min(boxes[-1])
    paper_out += a*b


print("Elves needs {} square feet of wrapping paper and {} feet of ribbon.".format(paper_out, ribbon_out))
