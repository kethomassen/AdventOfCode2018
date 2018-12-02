from collections import defaultdict

lines = []

with open("day2input.txt", "r") as f:
    for line in f.readlines():
        lines.append(line.rstrip('\n'))

two_count = 0
three_count = 0

for word in lines:
    counts = defaultdict(int)
    for letter in word:
        counts[letter] += 1
    has_two = False
    has_three = False
    for letter in counts:
        if counts[letter] == 2:
            has_two = True
        if counts[letter ] == 3:
            has_three = True
    if has_two:
        two_count += 1
    if has_three:
        three_count += 1

print(two_count*three_count)



