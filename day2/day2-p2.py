import re

# def process_lowest(each_pull: dict) -> tuple:
#     """
#     @param each_pull: dict of colors and how many times they were pulled
#     @return: tuple of highest of each color
#     """
#     answer = {'blue': 0,
#               'red': 0,
#               'green': 0}
#     for key, value in each_pull.items():
#         if 
#         match key:
#             case 'blue':
#                 if int(value) > 14:
#                     return False
#             case 'green':
#                 if int(value) > 13:
#                     return False
#             case 'red':
#                 if int(value) > 12:
#                     return False
#     return True


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