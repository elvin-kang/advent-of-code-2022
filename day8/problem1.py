grid = []

with open('input.txt', 'r') as fin:
    for line in fin:
        grid.append(list(map(int, line.strip())))


def is_visible_from_outside(grid, i, j):
    cur_height = grid[i][j]

    up_visible = True
    right_visible = True
    down_visible = True
    left_visible = True

    # up
    for up in range(i-1, -1, -1):
        if grid[up][j] >= cur_height:
            up_visible = False
            break

    # right
    for right in range(j+1, len(grid[0])):
        if grid[i][right] >= cur_height:
            right_visible = False
            break

    # down
    for down in range(i+1, len(grid)):
        if grid[down][j] >= cur_height:
            down_visible = False
            break

    # left
    for left in range(j-1, -1, -1):
        if grid[i][left] >= cur_height:
            left_visible = False
            break

    return any((up_visible, right_visible, down_visible, left_visible))


def count_visible(grid):
    count = len(grid) * 2 + (len(grid[0]) - 2) * 2

    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            if is_visible_from_outside(grid, i, j):
                count += 1

    return count


print(count_visible(grid))