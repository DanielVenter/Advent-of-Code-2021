import numpy as np

def step(array : list) -> list: 
    for i , line in enumerate(array):
        array[i] = [char + 1 for char in line]
    return(array)

def flashers(array : list) -> list:
    flash = []
    for y, line in enumerate(array):
        for x, line in enumerate(line):
            if array[y][x] > 9: 
                flash.append([x,y])
    return(flash)

def check_flash(array: list ,flasher : list) -> list:
    for flash in flasher:
        x , y = flash
        if x != 0 and y != 0:
            step(array[y -1 : y + 2, x -1 : x + 2])

        else:
            if x == 0 and y != 0:
                step(array[y - 1 : y + 2, x  : x + 2])
            elif x != 0 and y == 0:
                step(array[y : y + 2, x -1 : x + 2])
            else:
                step(array[y : y + 2, x  : x + 2])
        
        array[y][x] = 0

    return(array)      


with open("input.txt", "r") as f:
    lines = [line.strip("\n") for line in f]
    for i, n in enumerate(lines):
        lines[i] = [int(char) for char in n]

    lines = np.array(lines)

# The step counter
i = 0
zeros = lines.size - np.count_nonzero(lines)
while zeros != lines.size:
    step(lines)
    flashed = flashers(lines)
    done = flashers(lines)
    lines = check_flash(lines, flashed)  
    while flashed != []:
        flashed = flashers(lines)
        done += flashed
        lines = check_flash(lines, flashed)
    for d in done:
        x , y = d
        lines[y][x] = 0

    zeros = lines.size - np.count_nonzero(lines)
    i += 1
    
print(i)


    




    