input_chars = []

with open("day5input.txt", "r") as f:
    input_chars = list(f.readline().rstrip('\n'))

def get_length(chars):
    i = 0
    while i < (len(chars) - 1):
        diff = abs(ord(chars[i]) - ord(chars[i + 1]))
        if diff == 32:
            chars.pop(i+1)
            chars.pop(i)
            i = max(0, i-1)
        else:
            i += 1

    return len(chars)

alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
lengths = []

for letter in alphabet:
    lower_case = chr(ord(letter) + 32)
    new_input = [x for x in input_chars if x != letter and x != lower_case]
    
    lengths.append(get_length(new_input))

print(min(lengths))
