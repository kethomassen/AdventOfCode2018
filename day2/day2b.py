lines = []

with open("day2input.txt", "r") as f:
    for line in f.readlines():
        lines.append(line.rstrip('\n'))

found = False
for index, line in enumerate(lines):
    if found:
        break
    for search_index, search_line in enumerate(lines):
        if index == search_index:
            continue
        num_diff = 0
        diff_id = -1
        for i, letter in enumerate(line):
            if not line[i] == search_line[i]:
                num_diff += 1
                diff_id = i
        if num_diff == 1:
            found = True
            for i, letter in enumerate(line):
                if not i == diff_id:
                    print(letter, end="")

            break
