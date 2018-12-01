total = 0

with open("day1input.txt", "r") as f:
    for line in f.readlines():
        total += int(line.rstrip('\n'))

print(total)
