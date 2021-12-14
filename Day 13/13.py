def printLetters(array : list) -> str:
    joined = []
    for y in range(max(x[1] for x in array.keys())+1):
        line = []
        for x in range(max(x[0] for x in array.keys())+1):
            if (x,y) in array:
                line.append(array[(x,y)])
            else: 
                line.append(" ")
        joined.append("".join(line))

    return ("\n".join(joined))
    
with open("input.txt", 'r') as file: 
    points, folds = [x.splitlines() for x in file.read().split('\n\n')]
    grid = {tuple(int(z) for z in y.split(',')) : '#' for y in points}
    for i, instruction in enumerate(folds):
        inst = int(instruction.split()[-1].split('=')[-1])
        fold = [x for x in grid.keys() if x[0 if 'x' in instruction else 1] > inst]
        for point in fold:
            grid[(inst + (inst - point[0]), point[1]) if 'x' in instruction else (point[0], inst + (inst - point[1]))] = grid.pop(point)
        if i == 0:
            print(len(grid))



print(printLetters(grid))