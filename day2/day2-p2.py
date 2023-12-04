import re

def main():
    total = 0
    with open('data.txt', 'r', encoding='UTF-8') as data:
        for line in data.read().splitlines():
            game = [games.strip() for games in line.split(':')[1].split(';')]
            answer = {'blue': 0,
                      'red': 0,
                      'green': 0}
            for pulls in game:
                d = dict(tuple(reversed(match)) for match in re.findall(r'(\d+)\s+(\w+)', pulls))
                for k, v in d.items():
                    if answer[k] < int(v):
                        answer[k] = int(v)
            product = 1
            for v in answer.values():
                product *= v
            total += product
        print(total)


if __name__ == '__main__':
    main()