import statistics

def fuel_calc(position, ideal):
    movement = abs(position - ideal)
    fuel = (movement * (movement + 1)) // 2
    return fuel

def total_fuel(positions, ideal):
    total = 0
    for pos in positions:
        amount = fuel_calc(pos, ideal)
        total += amount  
    return total


with open ("input.txt", "r") as f:
    positions = list(map( int , f.readline().split(",")))


# Part 1 ideal value
ideal1 = int(statistics.median(positions))
# Part 2 ideal value
ideal2 = sum(positions) // len(positions)


fuel_pos = [0] * len(positions)


min_fuel = total_fuel(positions, ideal2)

print(min_fuel)





