chars = []

with open("day5input.txt", "r") as f:
    chars = list(f.readline().rstrip('\n'))

i = 0
while i < (len(chars) - 1):
    diff = abs(ord(chars[i]) - ord(chars[i + 1]))
    if diff == 32:
        chars.pop(i+1)
        chars.pop(i)
        i = max(0, i-1)
    else:
        i += 1

print(len(chars))
