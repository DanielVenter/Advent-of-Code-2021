from functools import reduce
from operator import mul

with open("input.txt", "r") as f:
    floor = [s.strip() for s in f.readlines()]

def height(xy):
    (x, y) = xy
    if 0 <= y < len(floor) and 0 <= x < len(floor[y]):
        return int(floor[y][x])
    else:
        return 10

def adjecents(xy):
    (x, y) = xy
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

def is_minima(xy):
    return all(height(xy) < height(adj_xy) for adj_xy in adjecents(xy))

def lowpoints():
    return ((x,y) for y in range(len(floor)) 
                  for x in range(len(floor[y])) 
                  if is_minima((x, y)))


print("part1", sum(height(xy) + 1 for xy in lowpoints()))


def basin(xy):
    return reduce(set.union, 
                 (basin(adj_xy) for adj_xy in adjecents(xy) 
                                if 9 > height(adj_xy) > height(xy)), 
                  set([xy]))

def basins():
    return [basin(lp) for lp in lowpoints()]

print("part2", reduce(mul, sorted((len(b) for b in basins()), reverse=True)[0:3], 1))