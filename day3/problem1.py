score = {chr(item): priority for item, priority in zip(range(ord('a'), ord('z')+1), range(1, 27))}

for item, priority in zip(range(ord('A'), ord('Z')+1), range(27, 53)):
    score[chr(item)] = priority

total = 0

with open('input.txt', 'r') as fin:
    for line in fin:
        line = line.strip()
        mid = len(line) // 2
        first = set(line[:mid])
        second = set(line[mid:])

        for item in first:
            if item in second:
                total += score[item]

print(total)