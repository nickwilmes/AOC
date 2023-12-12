from aocd import data
from dataclasses import dataclass
from enum import Enum
from collections import Counter


####################
# TEST DATA
####################
test_data = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

test_a_answer = "6440"
test_b_answer = "5905"


####################
# Puzzle solutions
####################


class HandType(Enum):
    UNKNOWN = 0
    HIGH = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


@dataclass
class Hand_A:
    cards: str
    bid: int
    type: HandType = HandType.UNKNOWN

    def __post_init__(self):
        counter = Counter(self.cards)
        triple_count = 0
        pair_count = 0
        for k, v in counter.most_common():
            if v == 5:
                self.type = HandType.FIVE_OF_A_KIND
                return
            elif v == 4:
                self.type = HandType.FOUR_OF_A_KIND
                return
            elif v == 3:
                triple_count += 1
            elif v == 2:
                pair_count += 1

        if triple_count == 1:
            if pair_count == 1:
                self.type = HandType.FULL_HOUSE
            else:
                self.type = HandType.THREE_OF_A_KIND

        elif pair_count == 2:
            self.type = HandType.TWO_PAIR
        elif pair_count == 1:
            self.type = HandType.PAIR

        else:
            self.type = HandType.HIGH


@dataclass
class Hand_B:
    cards: str
    bid: int
    type: HandType = HandType.UNKNOWN

    def __post_init__(self):
        counter = Counter(self.cards)
        triple_count = 0
        pair_count = 0

        jokers = counter.pop("J", 0)

        if jokers == 5:
            self.type = HandType.FIVE_OF_A_KIND
            return

        for k, v in counter.most_common():
            if v + jokers == 5:
                self.type = HandType.FIVE_OF_A_KIND
                return
            elif v + jokers == 4:
                self.type = HandType.FOUR_OF_A_KIND
                return
            elif v + jokers == 3:
                triple_count += 1
                jokers = 0
            elif v + jokers == 2:
                pair_count += 1
                jokers = 0

        if triple_count == 1:
            if pair_count == 1:
                self.type = HandType.FULL_HOUSE
            else:
                self.type = HandType.THREE_OF_A_KIND

        elif pair_count == 2:
            self.type = HandType.TWO_PAIR
        elif pair_count == 1:
            self.type = HandType.PAIR

        else:
            self.type = HandType.HIGH


def get_hand_hash_a(hand: Hand_A) -> float:
    hand_hash = hand.cards.replace("A", "E")
    hand_hash = hand_hash.replace("K", "D")
    hand_hash = hand_hash.replace("Q", "C")
    hand_hash = hand_hash.replace("J", "B")
    hand_hash = hand_hash.replace("T", "A")
    hand_hash = f"{hand.type.value}.{hand_hash}"
    return hand_hash


def get_hand_hash_b(hand: Hand_B) -> float:
    hand_hash = hand.cards.replace("A", "E")
    hand_hash = hand_hash.replace("K", "D")
    hand_hash = hand_hash.replace("Q", "C")
    hand_hash = hand_hash.replace("J", "0")
    hand_hash = hand_hash.replace("T", "A")
    hand_hash = f"{hand.type.value}.{hand_hash}"
    return hand_hash


def part_a(content: str):
    data = content.split("\n")

    hands = []
    for line in data:
        cards, bid = line.split()
        hands.append(Hand_A(cards, int(bid)))

    hands.sort(key=get_hand_hash_a)

    score = 0
    for i in range(len(hands)):
        score += hands[i].bid * (i + 1)

    return score


def part_b(content: str):
    data = content.split("\n")

    hands = []
    for line in data:
        cards, bid = line.split()
        hands.append(Hand_B(cards, int(bid)))

    hands.sort(key=get_hand_hash_b)

    score = 0
    for i in range(len(hands)):
        score += hands[i].bid * (i + 1)

    return score


####################
# Main Logic
####################
if __name__ == "__main__":
    content = data

    test_a = part_a(test_data)
    print(f"Test A: {test_a}")
    print(f"Part A answer: {part_a(content)}")
    assert str(test_a) == test_a_answer

    test_b = part_b(test_data)
    print(f"Test B: {test_b}")
    print(f"Part B answer: {part_b(content)}")
    assert str(test_b) == test_b_answer
