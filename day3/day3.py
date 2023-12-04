import sys

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']


def scan_array(array):
    total = 0
    for line_number, line in enumerate(array):
        buffer = []
        valid = False
        for index, item in enumerate(line):
            if item.isdigit():
                buffer.append(item)
                if ((line[index + 1] not in digits) or (array[line_number - 1][index - 1] not in digits)
                    or array[line_number - 1][index] not in digits or array[line_number - 1][index + 1]
                    not in digits or array[line_number + 1][index - 1] not in digits or 
                    array[line_number + 1][index] not in digits or array[line_number + 1][index + 1] not in digits
                    or line[index - 1] not in digits):
                    valid = True
            else:
                if buffer and valid:
                    total += int(''.join(buffer))
                    print(int(''.join(buffer)))
                buffer = []
                valid = False
    return total


def make_array(data) -> list[list[str]]:
    array = []
    array.append(list('.' * 141))
    for line in data:
        row = list(line.strip())
        row.insert(0, '.')
        row.append('.')
        array.append(row)
    array.append(list('.' * 141))
    return array


def main():
    total = 0
    with open('data.txt', 'r', encoding='UTF-8') as data:
        array = make_array(data)
    total = scan_array(array)
    print('\nTotal: ', total)


if __name__ == '__main__':
    main()