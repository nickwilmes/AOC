from aocd import data
import helpers
from typing import Optional
import re


# had to lookup a good solution for part B
# this vidoe had a great explaination:
# https://www.youtube.com/watch?v=-5J-DAsWuJc


####################
# TEST DATA
####################
test_data = """\
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""
test_b_data = test_data
test_a_answer = "480"
test_b_answer = "875318608908"

A_COST, B_COST = 3, 1
BUTTON_A, BUTTON_B = 1, 2
MAX_BUTTON_PRESS = 100

####################
# Puzzle solutions
####################
def part_a(content):
    machines = content.split("\n\n")
    winning_combos = []

    for m in machines:
        ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", m))
        ca = (px * by - py * bx) / (ax * by - ay * bx)
        cb = (px - ax * ca) / bx
        if ca % 1 == 0 and cb % 1 == 0 and ca <= 100 and cb <= 100:
            winning_combos.append(ca*A_COST+cb*B_COST)

    return int(sum(winning_combos))


def part_b(content):
    machines = content.split("\n\n")
    winning_combos = []

    for m in machines:
        ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", m))
        px += 10000000000000
        py += 10000000000000
        ca = (px * by - py * bx) / (ax * by - ay * bx)
        cb = (px - ax * ca) / bx
        if ca % 1 == 0 and cb % 1 == 0:
            winning_combos.append(ca*A_COST+cb*B_COST)

    return int(sum(winning_combos))


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
