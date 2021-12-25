import functools

def add(snNum1, snNum2):
    snSum = [[entry[0],entry[1]+1] for entry in snNum1 + snNum2]
    updated = True
    while updated:
        updated = False
        for i in range(len(snSum)):
            depth = snSum[i][1]
            if depth >= 5 and depth==snSum[i+1][1]:
                if i > 0:
                    snSum[i-1][0] += snSum[i][0]
                if i < len(snSum)-2:
                    snSum[i+2][0] += snSum[i+1][0]
                del snSum[i:i+2]
                snSum.insert(i,[0,depth-1])
                updated = True
                break
        if not updated:
            for i in range(len(snSum)):
                if snSum[i][0] > 9:
                    [val, depth] = snSum[i]
                    half_down = val//2
                    half_up = val - val//2
                    del snSum[i]
                    snSum.insert(i,[half_up, depth+1])
                    snSum.insert(i,[half_down, depth+1])
                    updated = True
                    break
    return snSum

def magnitude(snNum):
    while len(snNum) > 1:
        for i in range(len(snNum)):
            if i < len(snNum) - 1 and snNum[i][1] == snNum[i+1][1]:
                depth = snNum[i][1]
                val = snNum[i][0] * 3 + snNum[i+1][0] * 2
                del snNum[i:i+2]
                snNum.insert(i,[val,depth-1])
                break
    return snNum[0][0]



with open('input.txt', 'r') as f:
    lines= [line.strip() for line in f.readlines()]

processed = []
for line in lines:
    processed_line = []
    depth = 0
    for i in range(len(line)):
        if line[i] == '[':
            depth += 1
        elif line[i] ==  ']':
            depth -= 1
        elif line[i] == ',':
            pass
        else:
            processed_line.append([int(line[i]),depth])
    processed.append(processed_line)


res = 0
for i in range(len(processed)-1):
    for j in range(i+1, len(processed)):
        res = max(res, magnitude(add(processed[i], processed[j])))
        res = max(res, magnitude(add(processed[j], processed[i])))
print(res)
