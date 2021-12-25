with open("input.txt") as f:
        lines = f.read().split("inp w\n")[1:]

z = []  # number in base 26
max_num = [0] * 14
min_num = [0] * 14
for i, line in enumerate(lines):
    lines = line.split("\n")
    pop = int(lines[3][-2:]) == 26  # if digit should be popped from z
    x_add = int(lines[4].split()[-1])
    y_add = int(lines[14].split()[-1])

    if not pop:  # push digit to z
        z.append((i, y_add))
    else:  # apply restriction: last_z_digit == current_z_digit + difference
        j, y_add = z.pop()
        difference = x_add + y_add
        if difference < 0:
            max_num[i] = 9 + difference
            max_num[j] = 9
            min_num[i] = 1
            min_num[j] = 1 - difference
        elif difference > 0:
            max_num[i] = 9
            max_num[j] = 9 - difference
            min_num[i] = 1 + difference
            min_num[j] = 1
        else:
            max_num[i] = max_num[j] = 9
            min_num[i] = min_num[j] = 1

print("".join(map(str, max_num)))
print("".join(map(str, min_num)))