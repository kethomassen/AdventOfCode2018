lines = []

with open("day3input.txt", "r") as f:
    for line in f.readlines():
        details = []
        split = line.split(' ')
        details.append(int(split[0].lstrip('#')))
        coords = split[2].rstrip(':').split(',')
        details.extend([int(coords[0]), int(coords[1])])
        size = split[3].split('x')
        details.extend([int(size[0]), int(size[1])])
        lines.append(details)

grid = [[0 for i in range(1000)] for j in range(1000)]

for line in lines:
    for x in range(line[1], line[1] + line[3]):
        for y in range(line[2], line[2] + line[4]):
            grid[x][y] += 1

for line in lines:
    region = [grid[i][line[2]:(line[2]+line[4])] for i in range(line[1],line[1]+line[3])]
    if sum(sum(region, [])) == line[3]*line[4]:
        print(line[0])





