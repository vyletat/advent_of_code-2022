f = open("input.txt", "r")

result = 0
for line in f:
    rucksack = line.split()
    # split rucksack into two same parts
    rucksack1 = rucksack[:len(rucksack) // 2]
    rucksack2 = rucksack[len(rucksack) // 2:]
    # find same elements in both parts
    same = [x for x in rucksack1 if x in rucksack2]
    # if same is in interval [97, 122] them minus 96 and add to result
    for i in same:
        if 97 <= ord(i) <= 122:
            result += ord(i) - 96
        else:
            result += ord(i) - 38


