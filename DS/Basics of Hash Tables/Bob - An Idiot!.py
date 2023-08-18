n = int(input())

char_pos = {}
for i in range(256):
    char_pos[chr(i)] = chr(i)

for i in range(n):
    char1, char2 = input().split()

    char1_pos = char_pos.get(char1)
    char2_pos = char_pos.get(char2)

    char_pos[char1] = char2_pos
    char_pos[char2] = char1_pos

program = input()
translated_program = ""
for char in program:
    translated_program += char_pos.get(char)

print(translated_program)
