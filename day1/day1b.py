lines = []

with open("day1input.txt", "r") as f:
    for line in f.readlines():
        lines.append(int(line.rstrip('\n')))

frequencies = {}
found = False
freq = 0

while not found:
    for change in lines:
        freq += change
        if freq in frequencies:
            found = True
            break
        else:
            frequencies[freq] = 1

print(freq)
