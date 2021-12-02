with open("input.txt", "r") as f:
    lines = [lines.replace("\n","").split(" ") for lines in f.readlines()]

forward = 0
depth = 0
aim = 0 

for line in lines:
    if line[0] == "down":
        aim += int(line[1])
    elif line[0] == "up":
        aim -= int(line[1])
    else:
        forward += int(line[1])
        depth += int(line[1]) * aim
    
print(forward * depth)