from typing import List
from dataclasses import dataclass
from aocd import data
from collections import Counter, defaultdict


####################
# TEST DATA
####################
test_data = """\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""
test_a_answer = "1588"
test_b_answer = "2188189693529"


####################
# Puzzle solutions
####################
def part_a(content):
    string, rules = content.split('\n\n')
    rules = rules.strip().split('\n')

    for step in range(10):
        new_string = string[0]
        for i in range(1, len(string)):
            for rule in rules:
                pattern, insert = rule.split(" -> ")
                if pattern == string[i-1]+string[i]:
                    new_string += insert
            new_string += string[i]
        string = new_string

    counts = Counter(string).most_common()
    return counts[0][1] - counts[-1][1]


def part_b(content):
    string, rules = content.split('\n\n')
    rules = rules.strip().split('\n')
    rules_dict = defaultdict(lambda: '')
    for rule in rules:
        pattern, insert = rule.split(" -> ")
        rules_dict[pattern[0], pattern[1]] = insert

    counts = Counter()
    for i in range(0, len(string)-1):
        counts.update([(string[i], string[i+1])])

    for step in range(40):
        new_counts = Counter()
        for c in counts.most_common():
            pattern, count = c[0], c[1]
            if (insert := rules_dict[pattern]) != '':
                new_counts[(pattern[0], insert)] += count
                new_counts[(insert, pattern[1])] += count
            else:
                new_counts[pattern] += count
        counts = new_counts

    char_count = Counter()
    for pattern, amount in counts.most_common():
        char_count[pattern[0]] += amount
    char_count[string[-1]] += 1

    counts_mc = char_count.most_common()
    return counts_mc[0][1] - counts_mc[-1][1]


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
