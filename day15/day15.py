def get_input():
    strings = []
    with open('data.txt', 'r', encoding='UTF-8') as data:
        for line in data.read().splitlines():
                strings.extend(line.split(','))
    return strings


def hash_algorith(string):
    current = 0
    for char in string:
        current += ord(char)
        current *= 17
        current %= 256
    return current


def handle_hash_map(strings):
    hash_map = {}
    for i in range (256):
        hash_map[i] = []
    for string in strings:
        if '=' in string:
            string_hash = int(hash_algorith(string.split('=')[0]))
            if hash_map[string_hash]:
                already_there = 0
                for index in range(len((hash_map[string_hash]))):
                    if string.split('=')[0].replace('=', '') in hash_map[string_hash][index]:
                        already_there = True
                        replace_index = index
                if already_there:
                    hash_map[string_hash][replace_index] = string
                else:
                    hash_map[string_hash].append(string)
            else:
                hash_map[string_hash].append(string)
        else:
            string_hash = hash_algorith(string.replace('-', ''))
            for item in hash_map[string_hash]:
                if string.replace('-', '') in item:
                    hash_map[string_hash].remove(item)
    part_2 = 0
    for key, value in hash_map.items():
        for index, item in enumerate(value):
            part_2 += (key + 1) * (index + 1) * int(item.split('=')[1])
    return part_2


def main():
    strings = get_input()

    part_1 = 0
    for string in strings:
        part_1 += hash_algorith(string)
    print('Part 1 Total: ', part_1)

    part_2 = handle_hash_map(strings)
    print('Part 2 Total: ', part_2)


if __name__ == '__main__':
    main()
