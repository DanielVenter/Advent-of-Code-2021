import heapq
import fileinput

def get_neighbors(x : int, y : int, grid : list) -> list:
    neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    vals = []
    for dx, dy in neighbors:
        nx, ny = x+dx, y+dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            vals.append((nx, ny))
    return vals

def expand_grid(grid : list) -> list:
    rows, cols = len(grid), len(grid[0])
    big_grid = []
    for y in range(rows * 5):
        row = []
        for x in range(cols * 5):
            bx, by = x % cols, y % rows
            x_offset = x // cols
            y_offset = y // rows
            new_val = grid[y % cols][x % rows] + (x // cols) + (y // rows)
            while new_val > 9:
                new_val -= 9
            row.append(new_val)
        big_grid.append(row)
    return big_grid

def dijkstra(grid : list) -> int:
    start = (0, 0)
    end = (len(grid[0])-1, len(grid)-1)
    dist_heap = [(0, start)]
    visited = set()

    while dist_heap:
        dist, curr = heapq.heappop(dist_heap)
        if curr in visited:
            continue
        visited.add(curr)
        if curr == end:
            return dist

        for n in get_neighbors(curr[0], curr[1], grid):
            n_cost = grid[n[1]][n[0]] + dist
            heapq.heappush(dist_heap, (n_cost, n))


with open("input.txt", "r") as f:
    grid = [[int(char) for char in line.strip("\n")] for line in f.readlines()]

print(dijkstra(grid))
big_grid = expand_grid(grid)
print(dijkstra(big_grid))



