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

cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid

    def get_hand_kind(self, hand):
        counts = sorted([hand.count(i) for i in set(hand)])
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

    def get_joker_kind(self):
        return max([self.get_hand_kind(self.hand.replace("J", i)) for i in cards[:-1]])

    def __gt__(self, other):
        kind_a = self.get_joker_kind()
        kind_b = other.get_joker_kind()
        if kind_a != kind_b:
            return True if kind_a > kind_b else False
        for i, j in zip(self.hand, other.hand):
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
