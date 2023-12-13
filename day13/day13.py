def get_input():
    arrays = []
    array = []
    with open('data.txt', 'r', encoding='UTF-8') as data:
        for line in data.read().splitlines():
            if len(line) != 0:
                array.append(list(line))
            else:
                arrays.append(array)
                array = []
    return arrays


def transpose(arr):
    new_arr = []
    for i in range(len(arr[0])):
        row = []
        for item in arr:
            row.append(item[i])
        new_arr.append(row)
    return new_arr


def check_inflection(arr, index):
    i = 0
    while index - i > 0 and index + i < len(arr):
        if arr[index-i-1]==arr[index+i]:
            i += 1
            continue
        else:
            return False
    return True


def find_inflection(arr, part1_inflection=0):
    for i in range(len(arr[1:])):
        if arr[1:][i] == arr[i]:
            if check_inflection(arr, i+1):
                if i == part1_inflection - 1:
                    continue
                return i + 1
    return 0


def handle_smudges(mirror, part1_inflection):
    current = float('inf')
    for row_number, row in enumerate(mirror):
        for col_number, col in enumerate(row):
            new_reflection = 0
            if mirror[row_number][col_number] == "#":
                mirror[row_number][col_number] = "."
                new_reflection = find_inflection(mirror, part1_inflection)
                if new_reflection != 0 and new_reflection != part1_inflection:
                    current = new_reflection
                mirror[row_number][col_number] = "#"
            elif mirror[row_number][col_number] == ".":
                mirror[row_number][col_number] = "#"
                new_reflection = find_inflection(mirror, part1_inflection)
                if new_reflection != 0 and new_reflection != part1_inflection:
                    current = new_reflection
                mirror[row_number][col_number] = "."
    return current


def main():
    part_1 = 0
    part_2 = 0
    for arr in get_input():
        part1_inflection = find_inflection(arr)
        this_part1 = part1_inflection * 100
        part_1 += part1_inflection * 100
        if part1_inflection == 0:
            part1_inflection = find_inflection(transpose(arr))
            part_1 += part1_inflection
        inflection = handle_smudges(arr, part1_inflection) * 100
        if inflection == 0 or inflection == float('inf'):
            inflection = handle_smudges(transpose(arr), part1_inflection)
            if inflection == float('inf'):
                inflection = this_part1 // 100 or part1_inflection * 100
        part_2 += inflection
    print('Part 1 Answer: ', part_1)
    print('Part 2 Answer: ', part_2)

if __name__ == '__main__':
    main()
