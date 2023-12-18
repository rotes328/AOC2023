import numpy as np


def flood_fill(grid):
    stack = [(200, 300)]        # Trial and error, yet again

    while stack:
        x, y = stack.pop()

        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
            grid[x][y] = 1

            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))


def make_map(instructions):
    directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
    array = np.zeros((500, 500), dtype=int)   # Trial and error :)

    current_row, current_column = 200, 200    # Also trial and error :)

    for instruction in instructions:
        direction, steps = instruction[0], instruction[1]
        steps = int(steps)

        for _ in range(steps):
            delta_row, delta_col = directions[direction]
            current_row += delta_row
            current_column += delta_col
            array[current_row][current_column] = 1
    return array


def get_input():
    instructions = []
    with open('data.txt', 'r', encoding='UTF-8') as data:
        for line in data.read().splitlines():
            instructions.append([line.split()[0], line.split()[1]])
    return instructions


def main():
    instructions = get_input()
    array = make_map(instructions)
    flood_fill(array)
    print('Part 1 Answer: ', np.count_nonzero(array))


if __name__ == '__main__':
    main()
