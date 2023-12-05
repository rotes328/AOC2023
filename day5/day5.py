DATA_FOLDER = 'realdata'
MAP_ORDER = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light',
             'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']


def process_maps():
    return_dict = {}
    for map_name in MAP_ORDER:
        return_dict[map_name] = {}
        with open(f'{DATA_FOLDER}/{map_name}.txt', 'r', encoding='UTF-8') as data:
            for line in data.read().splitlines():
                dest = int(line.split()[0])
                source = int(line.split()[1])
                increment = int(line.split()[2])
                return_dict[map_name][f'range({source}, {source + increment})'] = dest - source
    return return_dict


def process_seeds(seeds, maps):
    answer = []
    for seed in seeds:
        for step in MAP_ORDER:
            for r in maps[step]:
                if seed in eval(r):
                    seed = seed + maps[step][r]
                    break
        answer.append(seed)
    return answer


def get_seeds():
    with open(f'{DATA_FOLDER}/seeds.txt', 'r', encoding='UTF-8') as data:
        seeds = [int(x) for x in data.read().split()]
    return seeds


def main():
    seeds = get_seeds()
    maps = process_maps()
    answer = process_seeds(seeds, maps)
    print(min(answer))


if __name__ == '__main__':
    main()