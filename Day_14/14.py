from collections import Counter, defaultdict
from math import ceil


with open("input.txt", "r") as file:
    lines = [line.strip("\n") for line in file.readlines()]


start = lines[0]
rules = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in lines[2:]}
count = Counter("".join(t) for t in zip(start, start[1:]))


END = 40

for _ in range(END):
    k = defaultdict(int)
    for pair, value in count.items():
        if pair in rules:
            i = rules[pair]
            k[pair[0]+i] += value
            k[i+pair[1]] += value
        else: 
            k[pair] = value
    
    count = k
    

count_char = defaultdict(int)
for pairs, value in count.items():
    count_char[pair[0]] += value
    count_char[pair[1]] += value

values = sorted(ceil(value/2) for value in count_char.values())
print(values[-1] - values[0])

