lines = []

with open("day3input.txt", "r") as f:
    for line in f.readlines():
        details = []
        split = line.split(' ')[2:]
        coords = split[0].rstrip(':').split(',')
        details.extend([int(coords[0]), int(coords[1])])
        size = split[1].split('x')
        details.extend([int(size[0]), int(size[1])])
        lines.append(details)

grid = [[0 for i in range(1000)] for j in range(1000)]

for line in lines:
    for x in range(line[0], line[0] + line[2]):
        for y in range(line[1], line[1] + line[3]):
            grid[x][y] += 1

total = 0

for row in grid:
    for value in row:
        if value > 1:
            total += 1

print(total)
