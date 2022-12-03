f = open("input.txt", "r")

result = 0
for line in f:
    rucksack = line.strip()
    # split rucksack into two same parts
    rucksack1, rucksack2 = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
    # find same elements in both parts
    same = [x for x in rucksack1 if x in rucksack2]
    # A - Z = 65 - 90 [27 - 57]
    # a - z = 97 - 122 [1 - 26]
    # if same is in interval [97, 122] them minus 96 and add to result
    for index, i in enumerate(same):
        # only first apearence of element is counted
        if index == 0:
            if 97 <= ord(i) <= 122:
                result += ord(i) - 96
            else:
                result += ord(i) - 38
        else:
            continue

print(result)
f.close()

# ------------------ Part 2 --------------------------

from itertools import islice

def next_n_lines(file_opened, N):
    return [x.strip() for x in islice(file_opened, N)]

lines_number = 3
resultGroup = 0
with open("input.txt", 'r') as f:
    while lines_number <= 300:
        lines = next_n_lines(f, 3)
        # find same elements in lines
        same = [x for x in lines[0] if x in lines[1] and x in lines[2]]
        for index, i in enumerate(same):
            # only first apearence of element is counted
            if index == 0:
                if 97 <= ord(i) <= 122:
                    resultGroup += ord(i) - 96
                else:
                    resultGroup += ord(i) - 38
            else:
                continue
        lines_number += 3

print(resultGroup)