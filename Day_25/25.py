def move(f,x):
    return {f(*p) if cucumbers[p] == x and f(*p) not in cucumbers else p : cucumbers[p] for p in cucumbers}


with open("input.txt") as f: 
    data = [line.strip("\n") for line in f.readlines()]

h , w = len(data), len(data[0])


cucumbers = {(r,c) : data[r][c] for r in range(h) for c in range(w) if data[r][c] != "."}


for turn in range(1000):
   cucumbers_before = cucumbers.copy()
   cucumbers = move(lambda r , c: (r, (c+1)%w) , ">")
   cucumbers = move(lambda r , c: ((r+1)%h, c) , "v")

   if cucumbers == cucumbers_before:
       print(turn+1)
       break