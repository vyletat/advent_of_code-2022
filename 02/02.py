f = open("input.txt", "r")

'''
Oponnent:
A - Rock
B - Paper
C - Scissors

Yor turn:
Y - Paper (2)
X - Scissors (3)
Z - Rock (1)

Score: 
Win: 6
Draw: 3
Lose: 0
'''

score = 0

'''
for line in file_input:
    line = line.strip()

    # read 2 values on line split by space
    values = line.split(" ")

    # if first value is A and second is Y
    if values[0] == "A" and values[1] == "Y":
        score += 8
    elif values[0] == "B" and values[1] == "X":
        score += 9
    elif values[0] == "C" and values[1] == "Z":
        score += 7

    # if first value is A and second is Z
    elif values[0] == "A" and values[1] == "Z":
        score += 4
    elif values[0] == "B" and values[1] == "Y":
        score += 5
    elif values[0] == "C" and values[1] == "X":
        score += 6

    else:
        # if second is Y
        if values[1] == "Y":
            score += 2
        # if second is X
        elif values[1] == "X":
            score += 3
        # if second is Z
        elif values[1] == "Z":
            score += 1

print(score)
'''

# First solution
ans1 = 0

for line in f:
    symbols = line.split()
    op, me = ord(symbols[0]) - ord("A"), ord(symbols[1]) - ord("X")
    result = (me - op + 1) % 3
    ans1 += 3 * (result) + me + 1

print(ans1)

ans2 = 0
f = open("input.txt")
for line in f:
    symbols = line.split()
    op, result = ord(symbols[0]) - ord("A"), ord(symbols[1]) - ord("X")
    me = (op + result - 1) % 3
    ans2 += 3 * result + me + 1

print(ans2)


# Second solution
with open('input.txt', 'r') as f:
    games = f.read().split('\n')

WIN = 6
DRAW = 3
LOSS = 0

ROCK = 1
PAPER = 2
SCISSORS = 3

game_scores = {
    'A X': DRAW + ROCK,
    'A Y': WIN + PAPER,
    'A Z': LOSS + SCISSORS,
    'B X': LOSS + ROCK,
    'B Y': DRAW + PAPER,
    'B Z': WIN + SCISSORS,
    'C X': WIN + ROCK,
    'C Y': LOSS + PAPER,
    'C Z': DRAW + SCISSORS,
}

print(f'Part 1: {sum([game_scores.get(game, 0) for game in games])}')

game_scores = {
    'A X': LOSS + SCISSORS,
    'A Y': DRAW + ROCK,
    'A Z': WIN + PAPER,
    'B X': LOSS + ROCK,
    'B Y': DRAW + PAPER,
    'B Z': WIN + SCISSORS,
    'C X': LOSS + PAPER,
    'C Y': DRAW + SCISSORS,
    'C Z': WIN + ROCK,
}

print(f'Part 2: {sum([game_scores.get(game, 0) for game in games])}')