import sys


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
    answer = 999999999999999999999999999999
    temp_seed = 999999999999999999999999999999
    eseed = ''
    for eval_seed in seeds:
        current = 999999999999999999999999999999
        for seed in eval(eval_seed):
            temp = seed
            print(f'\rEvaluating {seed}', end='')
            for step in MAP_ORDER:
                for r in maps[step]:
                    if seed in eval(r):
                        seed = seed + maps[step][r]
                        break
            # print(eval_seed)
            # answer = seed if seed < answer else answer
            # temp_seed = temp if seed < answer else temp_seed
            if seed < current:
                current = seed
                temp_seed = temp
        if current < answer:
            answer = current
            # temp_seed = temp
            eseed = eval_seed
        print(eseed, temp_seed, answer)
    # print(f'\n{answer}')
    # print(eseed, temp_seed, answer)
    return (eseed, temp_seed, answer)


def get_seeds():
    seeds = []
    with open(f'{DATA_FOLDER}/seeds.txt', 'r', encoding='UTF-8') as data:
        input_data = [int(x) for x in data.read().split()]
        # input_data = [int(x) for x in '2243400000 516150861'.split()]
        for i in range(0, len(input_data), 2):
            seeds.append(f'range({input_data[i]}, {input_data[i] + input_data[i + 1]}, 1000000)')
    return seeds

# essed = range(1901414562, 2417565423, 1000), seed = 2417564562, answer = 2009707
# not 412483449
# 1081908503
# 2010707
# 2016145
# 2008785

def main():
    seeds = get_seeds()
    print(seeds)
    # seeds = ['range(2243424562, 2417565423, 10000)']
    # seeds = ['range(2243400000, 2243440000, 1)']
    print(seeds)
    # sys.exit()
    maps = process_maps()
    eseed, seed, answer = process_seeds(seeds, maps)
    print(f'essed = {eseed}, seed = {seed}, answer = {answer}')


if __name__ == '__main__':
    main()