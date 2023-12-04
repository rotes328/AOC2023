# Doesn't work

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
gear = ['*']

def scan_array(array):
    buffer_array = []
    for line_number, line in enumerate(array):
        buffer = []
        valid = False
        gear_location = []
        for index, item in enumerate(line):
            if item.isdigit():
                buffer.append(item)
                if ((line[index + 1] not in digits) or (array[line_number - 1][index - 1] not in digits)
                    or array[line_number - 1][index] not in digits or array[line_number - 1][index + 1]
                    not in digits or array[line_number + 1][index - 1] not in digits or 
                    array[line_number + 1][index] not in digits or array[line_number + 1][index + 1] not in digits
                    or line[index - 1] not in digits):
                    if (line[index + 1] in gear):
                        gear_location = [line_number, index + 1]
                    elif array[line_number - 1][index - 1] in gear:
                        gear_location = [line_number - 1, index - 1]
                    elif array[line_number - 1][index] in gear:
                        gear_location = [line_number - 1, index]
                    elif array[line_number - 1][index + 1] in gear:
                        gear_location = [line_number - 1, index + 1]
                    elif array[line_number + 1][index - 1] in gear:
                        gear_location = [line_number + 1, index - 1]
                    elif array[line_number + 1][index] in gear:
                        gear_location = [line_number + 1, index]
                    elif array[line_number + 1][index + 1] in gear:
                        gear_location = [line_number + 1, index + 1]
                    elif line[index - 1] in gear:
                        gear_location = [line_number, index - 1]
            else:
                if buffer and gear_location:
                    first_number = int(''.join(buffer))
                    y, x = gear_location[0], gear_location[1]
                    yy, xx = gear_location[0], gear_location[1]
                    new_buffer = []
                    back_buffer = []
                    forward_buffer = []
                    # if first_number == 951:
                        # print('here we are')
                        # print(x, y)
                        # print(line[x-4:x+4])
                        # print(array[y+1][x+1])
                    if y == line_number - 1 and array[y+1][x] == '.':
                        # print(first_number) #and line[x+1].isdigit():
                        x += 1
                        while line[x].isdigit():
                            new_buffer.append(line[x])
                            x += 1
                    if y == line_number and x == index:

# [(951, 346), (790, 871), (306, 374), (961, 722), (835, 141), (690, 326), (324, 391), (540, 871), (962, 205), (26, 560), (141, 542), (809, 925), (78, 156), (161, 546), (980, 143), (830, 828), (329, 623), (795, 68), (47, 704), (806, 316), (483, 399), (4, 25), (145, 15), (671, 431), (821, 59), (669, 577), (876, 573), (985, 841), (736, 404), (877, 510), (888, 260), (57, 44), (151, 201), (537, 260), (512, 376), (393, 140), (713, 224), (823, 65), (98, 559), (583, 72)]
                        if line[x+1].isdigit():
                            x += 1
                            while line[x].isdigit():
                                new_buffer.append(line[x])
                                x += 1
                        elif array[y+1][x-1].isdigit():
                            x = x - 1
                            while array[y+1][x].isdigit():
                                new_buffer.append(array[y+1][x])
                                x += 1
                        elif array[y+1][x].isdigit():
                            while array[y+1][x].isdigit():
                                new_buffer.append(array[y+1][x])
                                x += 1     
                        elif array[y+1][x+1].isdigit():
                            x += 1
                            while array[y+1][x].isdigit():
                                new_buffer.append(array[y+1][x])
                                x += 1     
                    elif y == (line_number + 1):
                        if array[line_number + 1][x - 1].isdigit():
                            while array[line_number + 1][x - 1].isdigit():
                                new_buffer.append(array[line_number + 1][x - 1])
                                x -= 1
                            new_buffer = list(reversed(new_buffer))
                        elif array[line_number + 1][x + 1].isdigit():
                            while array[line_number + 1][x + 1].isdigit():
                                    new_buffer.append(array[line_number + 1][x + 1])
                                    x += 1
                            new_buffer = new_buffer
                        if array[line_number + 2][x - 1].isdigit():
                            while array[line_number + 2][x - 1].isdigit():
                                back_buffer.append(array[line_number + 2][x - 1])
                                x -= 1
                        if array[line_number + 2][xx].isdigit():
                            while array[line_number + 2][xx].isdigit():
                                forward_buffer.append(array[line_number + 2][xx])
                                xx += 1
                        elif array[line_number + 2][xx + 1].isdigit():
                            while array[line_number + 2][xx+ + 1].isdigit():
                                forward_buffer.append(array[line_number + 2][xx + 1])
                                xx += 1
                    if back_buffer and forward_buffer:
                        second_number = int(''.join(list(reversed(back_buffer)) + list(forward_buffer)))
                    elif back_buffer and not forward_buffer:
                        second_number = int(''.join(list(reversed(back_buffer))))
                    elif forward_buffer:
                        second_number = int(''.join(forward_buffer))
                    elif new_buffer:
                        second_number = int(''.join(new_buffer))
                    buffer_array.append((first_number, second_number))
                first_number = 0
                second_number = 0
                buffer = []
                gear_location = []
    return buffer_array


def process_pairs(pairs):
    total = 0
    for pair in pairs:
        # print(pair)
        total += (pair[0] * pair[1])
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
    # with open('data1.txt', 'a', encoding='UTF-8') as file:
    #     for line in array:
    #         file.write(''.join(line))
    #         file.write('\n')
    return array


def main():
    total = 0
    with open('data.txt', 'r', encoding='UTF-8') as data:
        array = make_array(data)
    valids = scan_array(array)
    # print(valids)
    valids = list((valid for valid in valids if 0 not in valid))
    valids = list(valid for valid in valids if valid[0] != valid[1])
    print(valids)
    # pairs = scan_array_again(array, valids)
    total = process_pairs(valids)
    print('\nTotal: ', total)


if __name__ == '__main__':
    main()