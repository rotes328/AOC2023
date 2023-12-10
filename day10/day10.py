from copy import copy


def get_input():
    array = []
    with open('data.txt', 'r', encoding='UTF-8') as data:
        for line in data.read().splitlines():
            array.append(list(line))
    return array


def find_start(array):
    for y in range(len(array)):
        for x in range(len(array[y])):
            if array[y][x] == 'S':
                return (y, x)

def find_path(array, y, x):
    steps = 1
    current = [y, x + 1]
    previous = [y, x]
    while array[current[0]][current[1]] != 'S':
        match array[current[0]][current[1]]:
            case '|':
                if previous[0] < current[0]:
                    previous = copy(current)
                    current[0] += 1
                else:
                    previous = copy(current)
                    current[0] -= 1
            case '-':
                if previous[1] < current[1]:
                    previous = copy(current)
                    current[1] += 1
                else:
                    previous = copy(current)
                    current[1] -= 1
            case 'L':
                if previous[0] < current[0]:
                    previous = copy(current)
                    current[1] += 1
                else:
                    previous = copy(current)
                    current[0] -= 1
            case 'J':
                if previous[1] < current[1]:
                    previous = copy(current)
                    current[0] -= 1
                else:
                    previous = copy(current)
                    current[1] -= 1
            case '7':
                if previous[1] < current[1]:
                    previous = copy(current)
                    current[0] += 1
                else:
                    previous = copy(current)
                    current[1] -= 1
            case 'F':
                if previous[1] > current[1]:
                    previous = copy(current)
                    current[0] += 1
                else:
                    previous = copy(current)
                    current[1] += 1
        steps += 1
    return int(steps / 2)


def main():
    array = get_input()
    print('Part 1 Answer:', find_path(array, *find_start(array)))


if __name__ == '__main__':
    main()
