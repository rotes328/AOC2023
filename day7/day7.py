class Hand:
    def __init__(self, cards: list):
        self.cards = cards
        self._handle_strings()
        self.cards = [int(card) for card in self.cards]
        self._count()
        self._rank()

    def __repr__(self):
        return str(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    def _handle_strings(self):
        """
        Map ace, king, etc. to points
        A, K, Q, J, T, 9
        """
        for index, item in enumerate(self.cards):
            if not item.isdigit():
                match item:
                    case 'T':
                        self.cards[index] = '10'
                    case 'J':
                        self.cards[index] = '11'
                    case 'Q':
                        self.cards[index] = '12'
                    case 'K':
                        self.cards[index] = '13'
                    case 'A':
                        self.cards[index] = '14'


    def _count(self):
        self.item_counts = {}
        for item in self.cards:
            if item in self.item_counts:
                self.item_counts[item] += 1
            else:
                self.item_counts[item] = 1

    def _rank(self):
        if set(self.item_counts.values()) == {5}:
            self.rank = 7
        elif set(self.item_counts.values()) == {4, 1}:
            self.rank = 6
        elif set(self.item_counts.values()) == {3, 2}:
            self.rank = 5
        elif set(self.item_counts.values()) == {3, 1, 1}:
            self.rank = 4
        elif sorted((self.item_counts.values())) == [1, 2, 2]:
            self.rank = 3
        elif sorted((self.item_counts.values())) == [1, 1, 1, 2]:
            self.rank = 2
        elif set(self.item_counts.values()) ==  {1, 1, 1, 1, 1}:
            self.rank = 1

    def __gt__(self, other):
        if self.rank > other.rank:
            return True
        elif self.rank < other.rank:
            return False
        elif self.rank == other.rank:
            for item1, item2 in zip(self, other):
                if item1 > item2:
                    return True
                if item2 > item1:
                    return False


class Jokers_Hand(Hand):
    def __init__(self, cards: list):
        cards = ['1' if card == 'J' else card for card in cards]
        super().__init__(cards)

    def _rank(self):

        if not self.item_counts.get(1) == 5:
            jokers = self.item_counts.pop(1, 0)
            most_common_item = max(self.item_counts, key=self.item_counts.get)
            self.item_counts[most_common_item] += jokers
        self.item_counts_string = {str(key): value for key, value in self.item_counts.items()}

        if set(self.item_counts.values()) == {5}:
            self.rank = 7
        elif set(self.item_counts.values()) == {4, 1}:
            self.rank = 6
        elif set(self.item_counts.values()) == {3, 2}:
            self.rank = 5
        elif set(self.item_counts.values()) == {3, 1, 1}:
            self.rank = 4
        elif sorted((self.item_counts.values())) == [1, 2, 2]:
            self.rank = 3
        elif sorted((self.item_counts.values())) == [1, 1, 1, 2]:
            self.rank = 2
        elif set(self.item_counts.values()) ==  {1, 1, 1, 1, 1}:
            self.rank = 1
        

def get_deck(jokers = False):
    with open('data.txt', 'r', encoding='UTF-8') as data:
        hands = {Hand(list(line.split()[0])) if not jokers else Jokers_Hand(list(line.split()[0])):
                 line.split()[1] for line in data.read().splitlines()}
    return hands


def get_score(hands_list_sorted, hands):
    score = 0
    for index, hand in enumerate(hands_list_sorted):
        score += (index + 1) * int(hands[hand])
    return score


def main():
    hands_1 = get_deck()
    hands_2 = get_deck(jokers=True)
    score1 = get_score(sorted([hand for hand in hands_1]), hands_1)
    score2 = get_score(sorted([hand for hand in hands_2]), hands_2)
    print('Part 1: ', score1)
    print('Part 2: ', score2)


if __name__ == '__main__':
    main()
