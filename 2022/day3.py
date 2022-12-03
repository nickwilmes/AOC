from typing import List, Tuple
from aocd import data


####################
# TEST DATA
####################
test_data = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
test_a_answer = "157"
test_b_answer = "70"


####################
# Puzzle solutions
####################
def convert_to_compartments(sack: str) -> Tuple[str, str]:
    return [sack[:len(sack)//2], sack[len(sack)//2:]]


def get_priority(x: str) -> int:
    score = ord(x) - 96
    if score <=0:
        score += 58
    return score

    
def part_a(content):
    errors = []
    for sack in content.splitlines():
        c1, c2 = convert_to_compartments(sack)
        matching = set(c1).intersection(set(c2))
        errors.extend(list(matching))

    return sum([get_priority(x) for x in errors])


def part_b(content):
    badges = []
    sacks = content.splitlines()
    for i in range(0, len(sacks), 3):
        common = set(sacks[i]).intersection(set(sacks[i+1]))
        badge = list(common.intersection(set(sacks[i+2])))[0]
        badges.append(badge)

    return sum([get_priority(x) for x in badges])
        


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
