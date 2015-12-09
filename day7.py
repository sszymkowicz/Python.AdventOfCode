def is_num(x) -> int:
    try:
        int(x)
        return 1
    except ValueError:
        return 0

with open("day7.txt") as f:
    lines = f.readlines()

values = dict()

while 'a' not in values:
    for i in lines:
        i_list = i.rstrip("\n").split(" ")

        if i_list[0] == "NOT" and i_list[1] in values:
            values[i_list[3]] = ~values[i_list[1]]
            lines.remove(i)
        elif i_list[1] == "->":
            try:
                values[i_list[2]] = int(i_list[0])
                lines.remove(i)
            except ValueError:
                if i_list[0] in values:
                    values[i_list[2]] = values[i_list[0]]
                    lines.remove(i)
        elif i_list[1] == "AND":
            num = is_num(i_list[0])
            if (i_list[0] in values or num) and \
                    i_list[2] in values:
                if not num:
                    values[i_list[4]] = values[i_list[0]] & values[i_list[2]]
                else:
                    values[i_list[4]] = int(i_list[0]) & values[i_list[2]]
        elif i_list[1] == "LSHIFT":
            num = is_num(i_list[2])
            if i_list[0] in values and \
                    (i_list[2] in values or num):
                if not num:
                    values[i_list[4]] = values[i_list[0]] << values[i_list[2]]
                else:
                    values[i_list[4]] = values[i_list[0]] << int(i_list[2])
        elif i_list[1] == "RSHIFT":
            num = is_num(i_list[2])
            if i_list[0] in values and \
                    (i_list[2] in values or num):
                if not num:
                    values[i_list[4]] = values[i_list[0]] >> values[i_list[2]]
                else:
                    values[i_list[4]] = values[i_list[0]] >> int(i_list[2])
        elif i_list[1] == "OR":
            num = is_num(i_list[0])
            if (i_list[0] in values or num) and \
                    i_list[2] in values:
                if not num:
                    values[i_list[4]] = values[i_list[0]] | values[i_list[2]]
                else:
                    values[i_list[4]] = int(i_list[0]) | values[i_list[2]]

print(values['a'])
