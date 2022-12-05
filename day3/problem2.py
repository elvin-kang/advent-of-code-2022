score = {chr(item): priority for item, priority in zip(range(ord('a'), ord('z')+1), range(1, 27))}

for item, priority in zip(range(ord('A'), ord('Z')+1), range(27, 53)):
    score[chr(item)] = priority

total = 0

with open('input.txt', 'r') as fin:
    while True:
        common = set()
        first = fin.readline().strip()
        if not first:
            break
        # assume we always have multiple of 3 lines
        second = set(fin.readline().strip())        
        for char in first:
            if char in second:
                common.add(char)

        third = fin.readline().strip()
        for char in third:
            if char in common:
                total += score[char]
                break

print(total)