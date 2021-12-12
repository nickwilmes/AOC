from aocd import data
import sys
from dataclasses import dataclass
import timeit


####################
# TEST DATA
####################
test_data = """\
FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
"""
test_a_answer = "820"
test_b_answer = ""


####################
# Puzzle solutions
####################
def pass_to_id(pp: str):
    row_b = pp[0:7].replace('B', '1').replace('F', '0')
    seat_b = pp[7:10].replace('R', '1').replace('L', '0')
    return int(row_b, 2)*8+int(seat_b, 2)


def part_a(content):
    highest = 0
    for pp in content:
        id = pass_to_id(pp)
        if id>highest:
            highest = id

    return highest


def part_b(content=None):
    ids = [pass_to_id(pp) for pp in content]
    ids.sort()
    for i in range(1, len(ids)):
        if ids[i-1] + 1 != ids[i]:
            my_id = ids[i]-1
            return my_id


####################
# Main Logic
####################
if __name__ == "__main__":
    content = data.splitlines()

    test_a = part_a(test_data.splitlines())
    print(f"Test A: {test_a}")
    print(f"Part A answer: {part_a(content)}")
    assert str(test_a) == test_a_answer

    # test_b = part_b(test_data.splitlines())
    # print(f"Test B: {test_b}")
    print(f"Part B answer: {part_b(content)}")  # 95476248 is too high
    # assert str(test_b) == test_b_answer

    # print(timeit.timeit('part_b()', "from __main__ import part_b", number=1))
