from typing import List
from aocd import data
import numpy as np


####################
# TEST DATA
####################
test_data = """\
Time:      7  15   30
Distance:  9  40  200"""

test_a_answer = "288"
test_b_answer = "71503"


####################
# Puzzle solutions
####################


def find_min(time: int, distance: int) -> int:
    min_win, max_win = time, 0
    i = int(time / 2)
    jump = int(time / 2)
    while max_win - 1 != min_win:
        if i * (time - i) > distance:
            min_win = min([i, min_win])
            max_win = max([i, max_win])
            i -= jump
        else:
            if jump == 1 and i + 1 == min_win:
                break
            i += jump
        jump = max([int(jump / 2), 1])

    return min_win


def part_a(content: str):
    data = content.split("\n")

    times = list(map(int, data[0].partition(":")[-1].split()))
    distances = list(map(int, data[1].partition(":")[-1].split()))

    options = []

    for i in range(len(times)):
        time = times[i]
        distance = distances[i]
        shortest_hold = find_min(time, distance)
        options.append((time + 1) - (2 * shortest_hold))

    return np.prod(options)


def part_b(content: str):
    data = content.split("\n")

    time = int(data[0].replace(" ", "").partition(":")[-1])
    distance = int(data[1].replace(" ", "").partition(":")[-1])

    shortest_hold = find_min(time, distance)
    options = (time + 1) - (2 * shortest_hold)

    return options

    return 0


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
