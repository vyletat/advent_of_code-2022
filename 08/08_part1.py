f = open("input.txt", "r")

current_x = 0
current_y = 0
grid = []

for line in f:
    line = line.strip()
    # load every char from line to list as number
    grid.append([int(x) for x in line])

MAX_Y = len(grid)
MAX_X = len(grid[0])

# ------------------ METHODS ------------------
def visible_top():
    current_tree = grid[current_x][current_y]
    trees = []
    if current_x == 0:
        return True
    else:
        for x in range(current_x - 1, -1, -1):
            trees.append(grid[x][current_y])
        # find if value current_tree is biggest in trees
        if current_tree > max(trees):
            return True
        else:
            return False


def visible_bottom():
    current_tree = grid[current_x][current_y]
    trees = []
    if current_x == MAX_Y - 1:
        return True
    else:
        for x in range(current_x + 1, MAX_Y, 1):
            trees.append(grid[x][current_y])
        # find if value current_tree is biggest in trees
        if current_tree > max(trees):
            return True
        else:
            return False


def visible_left():
    current_tree = grid[current_x][current_y]
    trees = []
    if current_y == 0:
        return True
    else:
        for y in range(current_y - 1, -1, -1):
            trees.append(grid[current_x][y])
        # find if value current_tree is biggest in trees
        if current_tree > max(trees):
            return True
        else:
            return False


def visible_right():
    current_tree = grid[current_x][current_y]
    trees = []
    if current_y == MAX_X - 1:
        return True
    else:
        for y in range(current_y + 1, MAX_X, 1):
            trees.append(grid[current_x][y])
        # find if value current_tree is biggest in trees
        if current_tree > max(trees):
            return True
        else:
            return False


# -------------- MAIN ----------------

count = 0
# iterate grid
for x in grid:
    current_x = grid.index(x)
    for y in x:
        # print(current_y)
        top = visible_top()
        bottom = visible_bottom()
        left = visible_left()
        right = visible_right()
        if top or bottom or left or right:
            count += 1
        current_y += 1
    current_y = 0

print(count)