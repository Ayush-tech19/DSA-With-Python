arr = [1, 2, 2, 3, 3, 3, 4]

freq = {}  # empty dictionary

for element in arr:
    if element in freq:
        freq[element] += 1
    else:
        freq[element] = 1

print("Frequency:", freq)