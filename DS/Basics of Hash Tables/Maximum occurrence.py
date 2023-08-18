s = input()

hash_table = [0 for _ in range(256)]

max_char = None
max_char_frequency = 0

for char in s:
    idx = ord(char)
    hash_table[idx] += 1

    if hash_table[idx] == max_char_frequency:
        if char < max_char:
            max_char = char
            max_char_frequency = hash_table[idx]

    if hash_table[idx] > max_char_frequency:
        max_char = char
        max_char_frequency = hash_table[idx]

print(f"{max_char} {max_char_frequency}")
