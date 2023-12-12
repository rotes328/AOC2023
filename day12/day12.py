
def get_input():
    springs = []
    with open('data.txt', 'r', encoding='UTF-8') as data:
        for line in data.read().splitlines():
            this_list = (tuple(int(c) for c in line.split()[1].split(','))), line.split()[0]
            springs.append(this_list)
    return springs

memo_dict = {}

def make_combinations(sequence):
    global memo_dict
    if '?' not in sequence:
        return [sequence]

    if sequence in memo_dict:
        return memo_dict[sequence]

    index = sequence.find('?')
    combinations_dot = make_combinations(sequence[:index] + '.' + sequence[index + 1:])
    combinations_hash = make_combinations(sequence[:index] + '#' + sequence[index + 1:])
    result = combinations_dot + combinations_hash

    # Memoize the result
    memo_dict[sequence] = result

    return result


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

    # for numbers, spring in springs:
    #     total += check(numbers, make_combinations(spring))
    # print(total)

    total = 0
    for numbers, springs in springs:
        total += check(numbers * 5, make_combinations('?'.join([springs] * 5)))
    print(total)
                

if __name__ == '__main__':
    main()