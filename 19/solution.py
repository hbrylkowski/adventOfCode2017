LEFT = 2
UP = 1
DOWN = -1
RIGHT = -2

directions = {
    UP: (0, -1),
    DOWN: (0, 1),
    LEFT: (-1, 0),
    RIGHT: (1, 0),
}


with open('input') as f:
    grid = [[c for c in l] for l in f.read().split("\n")]

grid_copy = [g[:] for g in grid]

y = 0
x = grid[0].index('|')
direction = DOWN
letters = ''
steps = 0

end = False
while not end:
    steps += 1
    x += directions[direction][0]
    y += directions[direction][1]
    if y < 0 or y >= len(grid):
        break
    elif x < 0 or x >= len(grid[y]):
        break
    grid_copy[y][x] = 'O'
    if grid[y][x].isalpha():
        letters += grid[y][x]
    elif grid[y][x] == ' ':
        break
    elif grid[y][x] == '+':
        for d in directions:
            if direction + d == 0:
                continue
            try:
                if grid[y + directions[d][1]][x + directions[d][0]] != ' ':
                    direction = d
                    break
            except IndexError:
                pass
print(letters)
print(steps)

