def get_input():
    array = []
    with open('data.txt', 'r', encoding='UTF-8') as data:
        for line in data.read().splitlines():
            array.append(list(line))
    return array


def find_gaps(universe, galaxies):
    x = []
    y = []
    for coordinates in galaxies.values():
        x.append(coordinates[0])
        y.append(coordinates[1])
    expand_x = []
    expand_y = []
    for xc in range(len(universe)):
        if xc not in x:
            expand_x.append(xc)
    for yc in range(len(universe)):
        if yc not in y:
            expand_y.append(yc)
    return expand_x, expand_y


def expand(galaxies, x_gaps, y_gaps, expansion_rate):
    return_galaxies = {}
    for key, value in galaxies.items():
        count_x = 0
        count_y = 0
        for x in x_gaps:
            if value[0] > x:
                count_x += 1
        for y in y_gaps:
            if value[1] > y:
                count_y += 1
        # Add to the coordinates of galaxies to expand them
        return_galaxies[key] = (value[0] + count_x * (expansion_rate - 1),
                                value[1] + count_y * (expansion_rate - 1))
    return return_galaxies


def find_galaxies(expanded_universe):
    galaxies = {}
    galaxy_number = 0
    for y, line in enumerate(expanded_universe):
        for x, item in enumerate(line):
            if item == '#':
                galaxies[galaxy_number] = (x, y)
                galaxy_number += 1
    return galaxies


def shortest_path(galaxies):
    current_galaxy = 0
    total = 0
    for i in range(len(galaxies)):
        for index in range(current_galaxy + 1, len(galaxies)):
            distance = abs(galaxies[index][0] - galaxies[current_galaxy][0]) + abs(galaxies[index][1] - galaxies[current_galaxy][1])
            total += distance
        current_galaxy += 1
    return total


def main():
    universe = get_input()
    galaxies = find_galaxies(universe)
    x_gaps, y_gaps = find_gaps(universe, galaxies)
    expanded_galaxies_1 = expand(galaxies, x_gaps=x_gaps, y_gaps=y_gaps, expansion_rate=2)
    print('Answer Part 1: ', shortest_path(expanded_galaxies_1))
    expanded_galaxies_2 = expand(galaxies, x_gaps=x_gaps, y_gaps=y_gaps, expansion_rate=1000000)
    print('Answer Part 2: ', shortest_path(expanded_galaxies_2))


if __name__ == '__main__':
    main()
