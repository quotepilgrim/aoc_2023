import sys

infile = sys.argv[1]
hands = []

hand_kinds = {
    "five-of-a-kind": 6,
    "four-of-a-kind": 5,
    "full-house": 4,
    "three-of-a-kind": 3,
    "two-pairs": 2,
    "one-pair": 1,
    "high-card": 0,
}

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


class Hand:
    def __init__(self, hand, bid):
        self.cards = hand
        self.bid = bid

    def get_hand_kind(self):
        counts = sorted([self.cards.count(i) for i in set(self.cards)])
        if 5 in counts:
            return hand_kinds["five-of-a-kind"]
        elif 4 in counts:
            return hand_kinds["four-of-a-kind"]
        elif 3 in counts and 2 in counts:
            return hand_kinds["full-house"]
        elif 3 in counts:
            return hand_kinds["three-of-a-kind"]
        elif counts.count(2) == 2:
            return hand_kinds["two-pairs"]
        elif 2 in counts:
            return hand_kinds["one-pair"]
        else:
            return hand_kinds["high-card"]

    def __gt__(self, other):
        kind_a = self.get_hand_kind()
        kind_b = other.get_hand_kind()
        if kind_a != kind_b:
            return True if kind_a > kind_b else False
        for i, j in zip(self.cards, other.cards):
            if i != j:
                return True if cards.index(i) < cards.index(j) else False


with open(infile) as f:
    for line in f:
        hand, bid = line.split()
        bid = int(bid)
        hands.append(Hand(hand, bid))

sorted_hands = sorted(hands)
winnings = [i.bid * (sorted_hands.index(i) + 1) for i in sorted_hands]

print(sum(winnings))
