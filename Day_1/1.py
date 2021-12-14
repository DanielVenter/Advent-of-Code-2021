with open("input.txt", "r") as f:
    lines = [int(l) for l in f.readlines()]

def count_increases(arr):
    prev = arr[0]
    increase_count = 0
    for v in arr[1:]:
        if v > prev:
            increase_count += 1
        prev = v
    return increase_count

def sliding_window(arr, size):
    sums = []
    for idx in range(size-1, len(arr)):
        sum = 0
        for offset in range(-size+1, 1):
            sum += lines[idx + offset]
        sums.append(sum)
    return sums

print(count_increases(lines))
print(count_increases(sliding_window(lines, 3)))