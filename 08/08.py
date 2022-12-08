f = open("input.txt", "r")

for line in f:
    line.strip()
    # load every char from line to list
    line = list(line)
