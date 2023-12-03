import re

def check_validity(each_pull: dict) -> bool:
    """
    @param each_pull: dict of colors and how many times they were pulled
    @return: True if valid, else False
    """
    for key, value in each_pull.items():
        match key:
            case 'blue':
                if int(value) > 14:
                    return False
            case 'green':
                if int(value) > 13:
                    return False
            case 'red':
                if int(value) > 12:
                    return False
    return True


def main():
    total = 0
    with open('data.txt', 'r', encoding='UTF-8') as data:
        for line in data.read().splitlines():
            game_valid = True
            game_number = int(re.search(r'\d+', line.split(':')[0]).group())
            game = [games.strip() for games in line.split(':')[1].split(';')]
            for pulls in game:
                if not check_validity(dict(tuple(reversed(match)) for match in re.findall(r'(\d+)\s+(\w+)', pulls))):
                    game_valid = False
                    break
            if game_valid:
                total += game_number
    print(total)


if __name__ == '__main__':
    main()