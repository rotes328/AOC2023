import numpy as np

def get_input():
    array = []
    with open('data.txt', 'r', encoding='UTF-8') as data:
        for line in data.read().splitlines():
                array.append(list(line))
    return array


def spin_cycle(arr):
    load_dict = {}
    cache = []
    pattern = {}
    for i in range(220):
        arr = shift_north(arr)
        arr = shift_west(arr)
        arr = shift_south(arr)
        arr = shift_east(arr)
        # Find a pattern
        load = get_load(arr)
        load_dict[i] = load
        if i > 140:
            if load not in cache:
                pattern[i] = load
            cache.append(load)
    # Fill in the blanks in pattern
    filled = {}
    for key in range(int([key for key in pattern.keys()][0]), int([key for key in pattern.keys()][-1])):
        filled[key] = load_dict[key]
    # Find start key
    for position in pattern:
        if position % len(filled) == 0:
            start = position
    return load_dict[start-(1000000000 % len(pattern))+1] # Otherwise off by one


def shift_north(arr):
    rotated = np.rot90(arr, 3)
    new_array = []
    for line in rotated:
        rocks = []
        new_line = []
        for i, c in enumerate(line):
            if c == '.':
                new_line.append(c)
            elif c == 'O':
                rocks.append(c)
            elif c == '#':
                new_line.extend(rocks)
                new_line.append(c)
                rocks = []
            if i == len(line) - 1:
                new_line.extend(rocks)
                rocks = []
        new_array.append(new_line)
    return np.rot90(np.array(new_array), 1)


def shift_south(arr):
    rotated = np.transpose(arr)
    new_array = []
    for line in rotated:
        rocks = []
        new_line = []
        for i, c in enumerate(line):
            if c == '.':
                new_line.append(c)
            elif c == 'O':
                rocks.append(c)
            elif c == '#':
                new_line.extend(rocks)
                new_line.append(c)
                rocks = []
            if i == len(line) - 1:
                new_line.extend(rocks)
                rocks = []
        new_array.append(new_line)
    return np.transpose(np.array(new_array))


def shift_west(arr):
    rotated = np.fliplr(arr)
    new_array = []
    for line in rotated:
        rocks = []
        new_line = []
        for i, c in enumerate(line):
            if c == '.':
                new_line.append(c)
            elif c == 'O':
                rocks.append(c)
            elif c == '#':
                new_line.extend(rocks)
                new_line.append(c)
                rocks = []
            if i == len(line) - 1:
                new_line.extend(rocks)
                rocks = []
        new_array.append(new_line)
    return np.fliplr(np.array(new_array))


def shift_east(arr):
    new_array = []
    for line in arr:
        rocks = []
        new_line = []
        for i, c in enumerate(line):
            if c == '.':
                new_line.append(c)
            elif c == 'O':
                rocks.append(c)
            elif c == '#':
                new_line.extend(rocks)
                new_line.append(c)
                rocks = []
            if i == len(line) - 1:
                new_line.extend(rocks)
                rocks = []
        new_array.append(new_line)
    return np.array(new_array)


def get_load(array):
    load = 0
    for line in np.fliplr(np.transpose(array)):
        for i, c in enumerate(line):
            if c == 'O':
                load += i + 1
    return load
            

def main():
    array = np.array(get_input())
    rocks = shift_north(array)
    load = get_load(rocks)
    print('Part 1 Answer: ', load)
    spin = spin_cycle(array)
    print('Part 2 Answer: ', spin)


if __name__ == '__main__':
    main()
