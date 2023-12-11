def get_input():
    array = []
    with open('data.txt', 'r', encoding='UTF-8') as data:
        for line in data.read().splitlines():
            array.append(list(line))
    return array


def find_gaps(universe, galaxies):
    x, y = zip(*galaxies.values())
    expand_x = [xc for xc in range(len(universe)) if xc not in x]
    expand_y = [yc for yc in range(len(universe)) if yc not in y]
    return expand_x, expand_y


def expand(galaxies, x_gaps, y_gaps, expansion_rate):
    return {key: (value[0] + sum(1 for x in x_gaps if value[0] > x) * (expansion_rate - 1),
                 value[1] + sum(1 for y in y_gaps if value[1] > y) * (expansion_rate - 1))
            for key, value in galaxies.items()}


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
    total = sum(abs(galaxies[j][0] - galaxies[i][0]) + abs(galaxies[j][1] - galaxies[i][1])
                for i in range(len(galaxies)) for j in range(i + 1, len(galaxies)))
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
