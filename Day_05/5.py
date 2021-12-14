import numpy as np

def line_horizontal(co):
    if co[0][1] == co[1][1]:
        return True
    else: return False

def line_vertical(co):
    if co[0][0] == co[1][0]:
        return True
    else: return False

def increasing(co):
    x1 = co[0][0]  
    x2 = co[1][0] 
    y1 = co[0][1]  
    y2 = co[1][1]
    if (y2-y1)/(x2-x1) > 0:
        return True
    else: return False


def add_lines(array, co):
    if line_horizontal(co):
        y = co[1][1]
        x1 = min(co[0][0], co[1][0])
        x2 = max(co[1][0] , co[0][0])
        line = array[y]
        for i in range(x1, x2 + 1):
            line[i] += 1
    elif line_vertical(co):
        ocean_t = array.transpose()
        x = co[0][0]
        y1 = min(co[0][1], co[1][1])
        y2 = max(co[1][1] , co[0][1])
        line = ocean_t[x]
        for i in range(y1, y2 + 1):
            line[i] += 1
        array = ocean_t.transpose()

    else:
        x1 = min(co[0][0], co[1][0])
        x2 = max(co[1][0] , co[0][0])
        y1 = min(co[0][1], co[1][1])
        y2 = max(co[1][1] , co[0][1])       
        
        if increasing(co):
            sub = array[y1:y2+1, x1:x2 +1]
            for i, line in enumerate(sub):
                line[i] += 1

        else:
            sub = array[y1:y2 + 1, x1:x2 + 1]
            for i, line in enumerate(reversed(sub)):
                line[i] += 1

    return(array)
    

with open("test.txt", "r") as f:
    cooridantes = []
    lines = [line.replace("\n", "") for line in f.readlines()]
    for line in lines:
        line = line.split(" ")        
        line.pop(1)
        line = [list(map(int ,char.split(","))) for char in line]
        cooridantes.append(line)


    sizeX = 0
    sizeY = 0

    for co in cooridantes:
        if max(co, key=lambda x: x[0])[0] > sizeX:
            sizeX = max(co, key=lambda x: x[0])[0]
        if max(co, key=lambda x: x[1])[1] > sizeY:
            sizeY = max(co, key=lambda x: x[1])[1]

    ocean_list = []
    for _ in range(sizeY + 1):
        line = [0] * (sizeX + 1)
        ocean_list.append(line)

    ocean = np.array(ocean_list)

    

    for co in cooridantes:
        ocean = add_lines(ocean, co)

    print(np.count_nonzero(ocean >= 2))





