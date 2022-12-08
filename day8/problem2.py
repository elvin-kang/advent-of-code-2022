grid = []

with open('input.txt', 'r') as fin:
    for line in fin:
        grid.append(list(map(int, line.strip())))


def calculate_scenic_score(grid, i, j):
    cur_height = grid[i][j]

    up_count = 0
    right_count = 0
    down_count = 0
    left_count = 0

    # up
    for up in range(i-1, -1, -1):
        up_count += 1
        if grid[up][j] >= cur_height:
            break

    # right
    for right in range(j+1, len(grid[0])):
        right_count += 1
        if grid[i][right] >= cur_height:
            break

    # down
    for down in range(i+1, len(grid)):
        down_count += 1
        if grid[down][j] >= cur_height:
            break

    # left
    for left in range(j-1, -1, -1):
        left_count += 1
        if grid[i][left] >= cur_height:
            break

    return up_count * right_count * down_count * left_count


def get_highest_scenic_score(grid):
    best_score = -float('inf')

    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            best_score = max(best_score, calculate_scenic_score(grid, i, j))

    return best_score


print(get_highest_scenic_score(grid))