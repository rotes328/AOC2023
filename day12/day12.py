def get_input():
    springs = []
    with open('data.txt', 'r', encoding='UTF-8') as data:
        for line in data.read().splitlines():
            this_list = (tuple(int(c) for c in line.split()[1].split(','))), line.split()[0]
            springs.append(this_list)
    return springs


def make_combinations(sequence):
    if '?' not in sequence:
        return [sequence]
    index = sequence.find('?')
    combinations_dot = make_combinations(sequence[:index] + '.' + sequence[index + 1:])
    combinations_hash = make_combinations(sequence[:index] + '#' + sequence[index + 1:])
    return combinations_dot + combinations_hash


def check(numbers, combinations):
    possible = 0
    for combination in combinations:
        if len([c for c in combination.split('.') if c != '']) != len(numbers):
            continue
        else:
            if tuple(map(len, [chars for chars in combination.split('.') if chars != ''])) == numbers:
                possible += 1
    return possible


def main():
    springs = get_input()
    total = 0

    for numbers, spring in springs:
        total += check(numbers, make_combinations(spring))
    print(total)

    # Part 2 is hard :(     

if __name__ == '__main__':
    main()