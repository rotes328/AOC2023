def get_input():
    array = []
    with open('data.txt', 'r', encoding='UTF-8') as data:
        for line in data.read().splitlines():
            array.append([int(x) for x in list(line.split())])
    return array


def analyze(line, arr=None):
    if arr is None:
        arr = [line]
    if all(element == 0 for element in line):
        return arr
    else:
        new_line = [line[i + 1] - line[i] for i in range(len(line) - 1)]
        arr.append(new_line)
        return analyze(new_line, arr)


def extrapolate(line, index=None):
    if index is None:
        index = len(line) - 1

    if index == 0:
        return line

    line[index - 1][-1] += line[index][-1]
    return extrapolate(line, index - 1)



def main():
    array = get_input()
    answer = 0
    for line in array:
        analyzed_list = analyze(line)
        analyzed_list[-1].append(0)
        answer += extrapolate(analyzed_list)[0][-1]
    print(answer)


if __name__ == '__main__':
    main()
