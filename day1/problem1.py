with open('calories.txt') as fin:
    all_calories = []
    cur_calories = 0
    for line in fin:
        if line.strip() == "":
            all_calories.append(cur_calories)
            cur_calories = 0
            continue
        cur_calories += int(line)

    

print(sum(sorted(all_calories)[-3:]))
