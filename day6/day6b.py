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
area = 0

for x in range (max_x+min_x):
    for y in range(max_y+min_y):
        total_dist = sum(list(map(lambda i: dist(i, (x, y)), coords)))
        
        if total_dist < 10000:
            area += 1

print(area)
