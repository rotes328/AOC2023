def get_deck():
    deck = []
    with open('data.txt', 'r', encoding='UTF-8') as data:
        for line in data.read().splitlines():
            number = int(line.split(':')[0].split()[1])
            winners = set(line.split(':')[1].split('|')[0].split())
            picks = set(line.split(':')[1].split('|')[1].split())
            deck.append((number, winners, picks))
    return deck


def process_cards(deck):
    counts = dict()
    for card in deck:
        counts[card[0]] = 1

    for card in deck:
        how_many = counts[card[0]]
        win_start = card[0] + 1
        win_end = card[0] + len(set(card[1] & set(card[2])))
        for _ in range(how_many):
            for i in range(win_start, win_end+1):
                counts[i] += 1

    return sum(counts.values())


def main():
    deck = get_deck()
    total = process_cards(deck)
    print(total)


if __name__ == '__main__':
    main()
