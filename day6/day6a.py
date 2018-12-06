from collections import Counter, defaultdict

coords = []

with open("day6input.txt", "r") as f:
    for line in f.readlines():
        split = line.rstrip("\n").split(", ")
        coords.append([int(split[0]), int(split[1])])

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

min_x = min(coords, key = lambda x: x[0])[0]
min_y = min(coords, key = lambda x: x[1])[1]
max_x = max(coords, key = lambda x: x[0])[0]
max_y = max(coords, key = lambda x: x[1])[1]

grid = [[-1 for i in range(max_y+min_y)] for j in range(max_x+min_x)]
borders = []

for x in range (max_x+min_x):
    for y in range(max_y+min_y):
        dists = dict((k, v) for k, v in enumerate(list(map(lambda i: dist(i, (x,y)), coords))))
        
        min_dist = min(dists.values())
        min_dists = dict((key, dists[key]) for key in dists if dists[key] == min_dist) 
       
        if len(min_dists) == 1:
            grid[x][y] = next(iter(min_dists)) 

            if x == 0 or y == 0 or x == max_x+min_x-1 or y == max_y+min_y-1:
                borders.append(next(iter(min_dists)))

flattened = [i for row in grid for i in row]
flattened = list(filter(lambda x: x not in borders and x != -1, flattened))
counter = Counter(flattened) 

print(max(counter.values()))
