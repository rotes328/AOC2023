from datetime import datetime

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
    answer = float('inf')
    temp_seed = float('inf')
    skip = 10000000
    eseed = ()
    for eval_seed in seeds:
        current = float('inf')
        for seed in range(eval_seed[0], eval_seed[1], skip):
            for step in MAP_ORDER:
                for r in maps[step]:
                    print(f'\rEvaluating {seed}', end='')
                    if seed in eval(r):
                        seed = seed + maps[step][r]
                        break
            if seed < current:
                current = seed
        if current < answer:
            answer = current
            eseed = eval_seed
    print('\n', eseed, skip)
    skip = int(skip / 10)
    while skip >= 1:
        current = 999999999999999999999999999999
        for seed in range(eseed[0], eseed[1], skip):
            temp = seed
            print(f'\rEvaluating {seed}', end='')
            for step in MAP_ORDER:
                for r in maps[step]:
                    if seed in eval(r):
                        seed = seed + maps[step][r]
                        break
            if seed < current:
                current = seed
                temp_seed = temp
        if current < answer:
            answer = current
        print('\n', temp_seed, eseed, skip)
        eseed = temp_seed - skip, temp_seed + skip
        skip = int(skip / 10)
    print()
    return answer


def get_seeds():
    seeds = []
    with open(f'{DATA_FOLDER}/seeds.txt', 'r', encoding='UTF-8') as data:
        input_data = [int(x) for x in data.read().split()]
        for i in range(0, len(input_data), 2):
            seeds.append((input_data[i], input_data[i] + input_data[i + 1]))
    return seeds

def main():
    start = datetime.now()
    seeds = get_seeds()
    maps = process_maps()
    answer = process_seeds(seeds, maps)
    print(f'Answer = {answer}')
    print(datetime.now() - start)


if __name__ == '__main__':
    main()