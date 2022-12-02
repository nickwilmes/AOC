from aocd import data
from typing import List


####################
# TEST DATA
####################
test_data = """\
A Y
B X
C Z
"""
test_a_answer = "15"
test_b_answer = "12"


####################
# Puzzle solutions
####################
SHAPE_SCORE_A = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}
SHAPE_SCORE_B = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 0,
    "Y": 3,
    "Z": 6,
}
def part_a(content):
    score = 0

    for round in content.splitlines():
        p1, p2 = unencrypt_round_a(round)
        score += p2
        score += get_result_score(p1, p2)
    
    return score
        

def get_result_score(p1: str, p2: str) -> int:
    if p1 == p2:
        return 3
    if p1 - p2 in [-1, 2]:
        return 6
    else:
        return 0


def unencrypt_round_a(data: str) -> List[int]:
    choices = data.split(" ")
    return [SHAPE_SCORE_A[x] for x in choices]


def unencrypt_round_b(data: str) -> List[int]:
    choices = data.split(" ")
    return [SHAPE_SCORE_B[x] for x in choices]


def part_b(content):
    score = 0

    for round in content.splitlines():
        p1, result = unencrypt_round_b(round)
        score += result
        score += find_move(p1, result)
    
    return score


def find_move(opp_choice: int, result: int):
    if result == 3:
        return opp_choice
    
    if result == 0:
        choice = opp_choice - 1
    else:
        choice = opp_choice + 1
    
    if choice == 0:
        choice = 3
    elif choice == 4:
        choice = 1

    return choice


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
