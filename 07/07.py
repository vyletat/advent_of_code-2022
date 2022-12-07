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


# make list of commands ['$ cd', '$ ls', '$ cd ..', '$ cd /', '$ cd', ]

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
# sum size of all elements
for element in elements:
     size += element.size
print(size)
