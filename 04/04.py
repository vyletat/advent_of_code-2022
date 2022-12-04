f = open("input.txt", "r")

count = 0
countOverlap = 0
for line in f:
    line.strip()
    # separate line by comma
    line = line.split(",")
    range1 = line[0].split("-")
    range2 = line[1].split("-")
    # do from range1[0] to range1[1] by 1 as list
    range1 = list(range(int(range1[0]), int(range1[1]) + 1, 1))
    range2 = list(range(int(range2[0]), int(range2[1]) + 1, 1))
    # find same elements in both ranges
    same = [x for x in range1 if x in range2]
    # if same elements are in range1 and range2 them add to count
    if same == range1 or same == range2:
        count += 1
    if len(same) > 0:
        countOverlap += 1

print(count)
print(countOverlap)
