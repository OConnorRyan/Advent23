import sys
list = []

for line in sys.stdin:
    #Starting from left of line, find first number
    for character in line:
        if character.isnumeric():
            char1 = character
            break

    for character in reversed(line):
        if character.isnumeric():
            char2 = character
            break
    
    list.append(int(char1 + char2))

print(sum(list))