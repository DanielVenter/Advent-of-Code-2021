with open("input.txt", "r") as f:
    lines =  f.readlines()[0]
    fishes = list(map(int, lines.split(","))) 

    states = {0: 0 , 1: 0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

    for fish in fishes:
        states[fish] += 1

    for _ in range(256):
        zeros = states[0]
        for i, key in enumerate(states):
            if i == 8:
                states[i] = zeros
                break
            if i == 6:
                states[i] = states[i + 1] + zeros            
            else:
                states[i] = states[i + 1]

print(sum(states.values()))



