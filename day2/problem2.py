ROCK = 1
PAPER = 2
SCISSORS = 3

LOST = 0
DRAW = 3
WIN = 6

col1 = {"A": ROCK, "B": PAPER, "C": SCISSORS}
# col2 = {"X": ROCK, "Y": PAPER, "Z": SCISSORS}

def calculate_point(opp, you):
    point = 0

    if you == "X":
        if opp == "A":
            point += SCISSORS
        elif opp == "B":
            point += ROCK
        elif opp == "C":
            point += PAPER
        return point
    elif you == "Y":
        return 3 + col1[opp]
    elif you == "Z":
        if opp == "A":
            point += PAPER
        elif opp == "B":
            point += SCISSORS
        elif opp == "C":
            point += ROCK
        return 6 + point
    else:
        raise ValueError("BAD INPUT")

total = 0

with open('input.txt') as fin:
    for line in fin:
        opp, you = line.strip().split()
        total += calculate_point(opp, you)

print(total)