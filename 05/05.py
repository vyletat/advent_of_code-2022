# Init stack
'''
        [C] [B] [H]
[W]     [D] [J] [Q] [B]
[P] [F] [Z] [F] [B] [L]
[G] [Z] [N] [P] [J] [S] [V]
[Z] [C] [H] [Z] [G] [T] [Z]     [C]
[V] [B] [M] [M] [C] [Q] [C] [G] [H]
[S] [V] [L] [D] [F] [F] [G] [L] [F]
[B] [J] [V] [L] [V] [G] [L] [N] [J]
 1   2   3   4   5   6   7   8   9
'''
# create crane key value pairs
storage = {
    1: ['B', 'S', 'V', 'Z', 'G', 'P', 'W'],
    2: ['J', 'V', 'B', 'C', 'Z', 'F'],
    3: ['V', 'L', 'M', 'H', 'N', 'Z', 'D', 'C'],
    4: ['L', 'D', 'M', 'Z', 'P', 'F', 'J', 'B'],
    5: ['V', 'F', 'C', 'G', 'J', 'B', 'Q', 'H'],
    6: ['G', 'F', 'Q', 'T', 'S', 'L', 'B'],
    7: ['L', 'G', 'C', 'Z', 'V'],
    8: ['N', 'L', 'G'],
    9: ['J', 'F', 'H', 'C']
}

f = open("input.txt", "r")

for line in f:
    line.strip()
    # get numbers from line
    line = [int(s) for s in line.split() if s.isdigit()]
    how_many = line[0]
    from_where = line[1]
    to_where = line[2]
    # get how many elements from storage[from_where] to storage[to_where]
    # and remove them from storage[from_where]
    # and add them to storage[to_where]
    for i in range(how_many):
        storage[to_where].append(storage[from_where].pop())

# print last element from each element in storage to one line
for i in storage:
    print(storage[i].pop(), end="")
print()
f.close()


# ----- Part 2 -----
# create crane key value pairs
storage = {
    1: ['B', 'S', 'V', 'Z', 'G', 'P', 'W'],
    2: ['J', 'V', 'B', 'C', 'Z', 'F'],
    3: ['V', 'L', 'M', 'H', 'N', 'Z', 'D', 'C'],
    4: ['L', 'D', 'M', 'Z', 'P', 'F', 'J', 'B'],
    5: ['V', 'F', 'C', 'G', 'J', 'B', 'Q', 'H'],
    6: ['G', 'F', 'Q', 'T', 'S', 'L', 'B'],
    7: ['L', 'G', 'C', 'Z', 'V'],
    8: ['N', 'L', 'G'],
    9: ['J', 'F', 'H', 'C']
}

f = open("input.txt", "r")

for line in f:
    line.strip()
    # get numbers from line
    line = [int(s) for s in line.split() if s.isdigit()]
    how_many = line[0]
    from_where = line[1]
    to_where = line[2]
    # get how many elements from storage[from_where] to storage[to_where]
    # and remove them from storage[from_where]
    # and add them to storage[to_where]
    cargo = []
    for i in range(how_many):
        # get how many elements from storage[from_where] and add them to cargo
        cargo.append(storage[from_where].pop())
    # reverse cargo
    cargo.reverse()
    # add each element from cargo to storage[to_where]
    for j in cargo:
        storage[to_where].append(j)

# print last element from each element in storage to one line
for i in storage:
    print(storage[i].pop(), end="")
f.close()