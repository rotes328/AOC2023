def find_possibilities(input_values):
    result = 1
    for time in input_values:
        hold = 1
        possibilities = 0
        while hold < time:
            distance = (time - hold) * hold
            hold += 1
            possibilities += 1 if distance > input_values[time] else 0
        result = result * possibilities
    return result


if __name__ == '__main__':
    input_values_p1 = {45: 305, 97: 1062, 72: 1110, 95: 1695}
    input_values_p2 = {45977295: 305106211101695}
    print('Answer 1: ', find_possibilities(input_values_p1))
    print('Answer 2: ', find_possibilities(input_values_p2))
