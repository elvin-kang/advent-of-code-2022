total = 0

with open('input.txt', 'r') as fin:
    for line in fin:
        first, second = line.strip().split(",")
        
        start1, end1 = map(int, first.split("-"))
        start2, end2 = map(int, second.split("-"))

        if min(end1, end2) - max(start1, start2) >= 0:
            total += 1

print(total)