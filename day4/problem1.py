total = 0

with open('input.txt', 'r') as fin:
    for line in fin:
        first, second = line.strip().split(",")
        
        start1, end1 = map(int, first.split("-"))
        start2, end2 = map(int, second.split("-"))

        if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
            total += 1

print(total)