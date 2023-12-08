import math


def get_network():
    with open('data.txt', 'r', encoding='UTF-8') as data:
        network = {}
        path = data.readline().strip()
        data.readline()
        for line in data.read().splitlines():
            key, value = map(str.strip, line.split('='))
            network[key] = tuple(val.strip('() ') for val in value.split(','))
    return path, network


def format_path(path):
    path = list(path)
    return [int(turn.replace('L', '0').replace('R', '1')) for turn in path]


def evaulate_network(node, path, network):
    steps = 0
    i = 0
    while not node.endswith('Z'):
        node = network[node][path[i]]
        steps += 1
        i = (i + 1) % len(path)
    return steps


def main():
    path, network = get_network()
    path = format_path(path)
    print('Steps in Part 1:', evaulate_network('AAA', path, network))
    print('Steps in Part 2:', math.lcm(*[evaulate_network(node, path, network) for node
                                       in network.keys() if node.endswith('A')]))

if __name__ == '__main__':
    main()
