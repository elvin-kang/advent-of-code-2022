ROCK = 1
PAPER = 2
SCISSORS = 3

LOST = 0
DRAW = 3
WIN = 6

col1 = {"A": ROCK, "B": PAPER, "C": SCISSORS}
col2 = {"X": ROCK, "Y": PAPER, "Z": SCISSORS}

def calculate_point(opp, you):
    if col1[opp] == col2[you]:
        return DRAW + col2[you]

    if col1[opp] + 1 == col2[you] or (opp == "C" and you == "X"):
        return WIN + col2[you]

    if col1[opp] == col2[you] + 1 or (opp == "A" and you == "Z"):
        return col2[you]

    raise ValueError("WRONG LOGIC")

total = 0

with open('input.txt') as fin:
    for line in fin:
        opp, you = line.strip().split()
        total += calculate_point(opp, you)

print(total)