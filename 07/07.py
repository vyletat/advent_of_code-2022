'''
f = open("input.txt", "r")

# make elemnts of with atributes:
#   - type: str
#   - name: str
#   - size: int
#   - other: list of other elements
class Element:
    def __init__(self, type, name, size, parent):
        self.type = type
        self.name = name
        self.size = size
        self.parent = parent


elements = [Element("dir", "/", 0, None)]
curent_dir = elements[0]
level = 0

for line in f:
    line.strip()
    # if line starts with '$'
    if line[0] == '$':
        # split line by ' ' and delete first element
        command = line.split(' ')
        # if command is 'cd'
        if command[1] == 'cd':
            # if command is '/..'
            if command[2] == '..':
                curent_dir = curent_dir.parent
                level -= 1
            elif command[2] == '/':
                curent_dir = elements[0]
                level = 0
            else:
                # find element with parent = curent_dir and name = command[2]
                for element in elements:
                    if element.parent == curent_dir and element.name == command[2]:
                        curent_dir = element
                        level += 1
                        break
        # if command is 'ls'
        elif command[1] == 'ls':
            break
    else:
        # split line by ' '
        line = line.split(' ')
        #if fist element is 'dir'
        if line[0] == 'dir':
            # make new element
            new_element = Element(line[0], line[1], 0, curent_dir)
            # add new element to elements
            elements.append(new_element)
        else:
            # make new element
            new_element = Element('file', line[1], int(line[0]), curent_dir)
            # add new element to elements
            elements.append(new_element)

size = 0
# find all elements with type = 'dir' from second element
for element in elements[1:]:
    if element.type == 'dir':
        # find all elements with parent = element
        for child in elements:
            if child.parent == element:
                # add size of child to size of element
                element.size += child.size
        # if element.size is <= 100000
        if element.size <= 100000:
            # add element.size to size
            size += element.size

print(size)
'''

from __future__ import annotations

class Directory:
    def __init__(self, name: str, parent: Directory | None) -> None:
        self.name = name
        self.parent = parent or self
        self.subs: dict[str, Directory] = {}
        self.files: dict[str, int] = {}

    def size(self) -> int:
        return sum(d.size() for d in self.subs.values()) + sum(self.files.values())

    def recursive_subs(self) -> set[Directory]:
        return {self}.union(*(sub.recursive_subs() for sub in self.subs.values()))


input = open("input.txt").readlines()

cwd = root = Directory("/", None)
for line in input:
    match line.split():
        case ["$", "cd", "/"]:
            cwd = root
        case ["$", "cd", ".."]:
            cwd = cwd.parent
        case ["$", "cd", sub]:
            cwd = cwd.subs.setdefault(sub, Directory(sub, cwd))
        case ["$", _]:
            pass
        case ["dir", sub]:
            cwd.subs[sub] = Directory(sub, cwd)
        case [size, file_name]:
            cwd.files[file_name] = int(size)

part1_result = sum(d.size() for d in root.recursive_subs() if d.size() <= 100000)
print(f"Result 1: {part1_result}")


size_threshold = 30000000 - 70000000 + root.size()
min_ = root.size()
for d in root.recursive_subs():
    min_ = min(min_, d.size()) if d.size() >= size_threshold else min_
print(f"Result 2: {min_}")